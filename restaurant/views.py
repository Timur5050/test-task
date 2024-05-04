from django.forms import model_to_dict
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
        lst = Restaurant.objects.all()
        return Response({'restaurants': RestaurantSerializer(lst, many=True).data})

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        restaurant_new = Restaurant.objects.create(
            id_restaurant=request.data['id_restaurant'],
            name_restaurant=request.data['name_restaurant'],
        )
        return Response({'restaurant': RestaurantSerializer(restaurant_new).data})
