# Booking-Platform-API

Design an API driven Ticket Booking Platform 

## To run this app locally

1. Install Python2.7 : https://www.python.org/downloads/
2. Install pip for python <br>
	`sudo apt-get update` <br>
	`sudo apt-get install python-pip`<br>
3. Install Virtual Environment<br>
	`sudo pip install virtualenv`<br>
4. Extract the Zip Folder<br>
	`cd UdaanAPI `<br>
5. Create Virtual Environment<br>
	`virtualenv venv`<br>
6. Activate the Virtual Environment<br>
	`source venv/bin/activate`<br>
	`pip install -r requirements.txt`<br>
	`python manage.py makemigrations`<br>
	`python manage.py migrate`<br>
	`python manage.py runserver 9090`<br>
Server will start -  127.0.0.1:9090<br>

### Test this API on POSTMAN<br>

After starting the server, copy http://127.0.0.1:9090/screens in POSTMAN <br>
Select request method as "GET" or "POST" as mentioned in the question.<br>
For <b>POST </b> request - Select JSON data type and write the Request body their as per the norms mentioned in the question and send the request, a Status : 201 created will be shown<br>
For <b>GET </b> request - Write the parameter as mentioned in the question, a JSON response can be will be displayed in the body.<br>
