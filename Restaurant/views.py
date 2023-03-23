from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

class showmenu(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    

class MenuItemByID(generics.RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    lookup_field='pk'


@permission_classes([IsAuthenticated])
class BookingsDone(generics.ListCreateAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer

class MyBooking(generics.RetrieveUpdateDestroyAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    lookup_field='Name'


