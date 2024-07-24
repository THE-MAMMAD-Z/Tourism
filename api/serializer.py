from rest_framework import serializers
from home.models import Place 
from account.models import CustomUser


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', "email" , "full_name" , "phone_number",'date_joined','password')


class PlaceSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('name', "phone" , "address" , "rate","city",'created_time','location_type')
