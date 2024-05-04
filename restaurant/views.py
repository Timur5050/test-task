from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant, Employee, Menu
from .serializers import RestaurantSerializer, EmployeeSerializer, MenuSerializer


class RestaurantAPIView(APIView):
    def get(self, request):
        lst = Restaurant.objects.all()
        return Response({'restaurants': RestaurantSerializer(lst, many=True).data})

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'restaurant': serializer.data})


class EmployeeAPIView(APIView):
    def get(self, request):
        lst = Employee.objects.all()
        return Response({'Employees': EmployeeSerializer(lst, many=True).data})

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Employee': serializer.data})


class MenuAPIView(APIView):
    def get(self, request):
        lst = Menu.objects.all()
        return Response({'Menus': MenuSerializer(lst, many=True).data})

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Menus': serializer.data})
