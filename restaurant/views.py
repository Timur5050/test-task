from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant
from .serializers import RestaurantSerializer


# Create your views here.

# class RestaurantAPIView(generics.ListAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer
class RestaurantAPIView(APIView):
    def get(self, request):
        return Response({'restaurant_id': '1'})

