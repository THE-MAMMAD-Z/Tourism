from django.shortcuts import render
from .serializer import PlaceSerialiser , UserSerialiser 
from django.contrib.auth.models import User
from home.models import Place
from account.models import CustomUser
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListCreateAPIView 

class PlaceList(ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class =PlaceSerialiser


class PlaceDetail(RetrieveUpdateDestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerialiser


class UserList(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class =UserSerialiser


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerialiser