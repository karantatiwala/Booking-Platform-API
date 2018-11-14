from django.contrib import admin
from .models import *

# Register your models here.

class TheatreDetailsData(admin.ModelAdmin):
	list_display = ('screenName', 'rowNumber','maxCapacity', 'bookedSeats')


admin.site.register(TheatreDetails, TheatreDetailsData)