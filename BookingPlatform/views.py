# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from BookingPlatform.models import TheatreDetails
from BookingPlatform.serializers import TheatreDetailsSerializer
import json


# Function that takes input as POST request for Storing information
# of Theatre Screens in Database
@api_view(['POST'])
def ScreenInput(request): 
	if request.method == 'POST':
		reqData = json.loads(request.body) 								#Converting the request to JSON form
		for rowNum in reqData["seatinfo"]:
			totalSeats = reqData["seatinfo"][rowNum]["numberOfSeats"]
			aisleSeats = reqData["seatinfo"][rowNum]["aisleSeats"]
			rowSeats = []
			for mark in range(0,totalSeats): 							#Marking seats as 0 - if vacant, -1 - if vacant and aisle seat
				rowSeats.append(0)
				if mark in aisleSeats:
					rowSeats[mark] = -1;
			rowSeats = json.dumps(rowSeats)
			obj = TheatreDetails(screenName=reqData["name"], rowNumber=rowNum, maxCapacity=totalSeats, bookedSeats=rowSeats)
			obj.save()
		return Response(status=201) 				# Sending the Success Response
	return Response(status=status.HTTP_400_BAD_REQUEST) 				# 400 Response if, not found



# Funtion to Book seats, requested by user and check
# if it is booked or not
@api_view(['POST'])
def reserveSeats(request, screen=None):
	if request.method == 'POST':
		reqData = json.loads(request.body) 							#Converting the request to JSON form
		flag = 0
		for i in reqData["seats"]:
			chk = TheatreDetails.objects.filter(screenName=screen, rowNumber=i).first()
			book = json.loads(chk.bookedSeats)
			for j in reqData["seats"][i]: 							#Checking if seats can be reserved or it is already booked
				if book[j] == 0 or book[j] == -1:
					flag =0
				else:
					flag=1
					break;
		if flag == 0: 												#Booking the seats, If all seats requested by user are available
			for i in reqData["seats"]:
				chk = TheatreDetails.objects.filter(screenName=screen, rowNumber=i).first()
				print chk.bookedSeats
				book = json.loads(chk.bookedSeats)
				for j in reqData["seats"][i]:
					if book[j] == -1:
						book[j] = 2  								#Marking aisle seats as 2, so as to differentiate from other seats
					elif book[j] == 0:
						book[j] = 1  								#Marking other seats as 1
				book = json.dumps(book)
				TheatreDetails.objects.filter(screenName=screen,rowNumber=i).update(bookedSeats=book)
			return Response(status=201) 							#Sending Success Response, if booked
		else:
			return Response(status=203) 							#Sending Response for Un-Authoriszed Request
	return Response(status=status.HTTP_400_BAD_REQUEST) 



# Function to get status of unreserved seats and for the user
# to check if he/she can book his/her desired seats
# Same function for API-3 and API-4
@api_view(['GET'])
def CheckSeatAvailability(request, screen=None):
	if request.method == 'GET':
		if request.GET.get('status', '') != '': 					#Checking if it for unreserved seats or desired seats
			chk = TheatreDetails.objects.filter(screenName=screen) 	#Creating an object the desired screen
			rowCheck = {}
			for i in chk:
				unresereRows =[]
				unreserve = json.loads(i.bookedSeats)
				for j in range(0, len(unreserve)):
					if unreserve[j] == 0 or unreserve[j] == -1: 	#Checking if the seat is booked or not
						unresereRows.append(j)
				rowCheck[i.rowNumber] = unresereRows
			seatCheck={}
			seatCheck["seats"] = rowCheck 							#Creating a dictionary of Unreserved Seats
			return JsonResponse(seatCheck) 							#Sending a JSON Response

		elif request.GET['numSeats'] and request.GET['choice']: 	#Checking is it is for Desired seats or not
			window = int(request.GET.get('numSeats')) 				#Extracting number of required seats from parameters
			choice = request.GET['choice'] 							#Extracting the choice of rows and seat number from parameters
			row, num = str(choice[0]), int(choice[1:])
			chk = TheatreDetails.objects.filter(screenName=screen, rowNumber=row).first() #Creating an object the desired screen and row number
			book = json.loads(chk.bookedSeats)
			result={}
			for i in range(num-window+1, num+1): 					#Using the Sliding window protocol, creating the subsets of desired seats
				l = book[i: i+window]
				if 2 in l or 1 in l: 								#Checking if the subsets contains reserved seats or not
					pass
				elif -1 in l: 										#checking if it contains aisle seats
					if l[-1] == -1 and l.count(-1)==1: 				#checking if it contains 1 aisle seat and is the last one in subset
						seats = []
						for j in range(i, i+window):
							seats.append(j)
						result[row] = seats 						#Appending that to result, that is to be shown
					else: 											#Checking if it contains more than 1 aisle seats
						pass
				else: 												#Checking if it contains all unreserved seats
					seats = []
					for j in range(i, i+window):
						seats.append(j)
					result[row] = seats
			if len(result) == 0: 
				error = "No Seats Available as per your requirements" #If the row does not have required seats
				return JsonResponse({"Error" : error})
			else:
				return JsonResponse({"availableSeats": result}) 	  #If it has desired seats, showing any one of desired outputs
	return Response(status=status.HTTP_400_BAD_REQUEST)
