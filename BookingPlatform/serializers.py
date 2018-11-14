from rest_framework import serializers
from .models import TheatreDetails

class TheatreDetailsSerializer(serializers.ModelSerializer):

	class Meta:
		model = TheatreDetails
		fields = '__all__'