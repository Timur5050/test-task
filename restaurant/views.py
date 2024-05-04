from datetime import datetime

from django.forms import model_to_dict
from django.utils import timezone
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

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Employee.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = EmployeeSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})


class MenuAPIView(APIView):
    def get(self, request):
        lst = Menu.objects.all()
        return Response({'Menus': MenuSerializer(lst, many=True).data})

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Menus': serializer.data})

# http://127.0.0.1:8000/api/v1/getResultOfCurrentDay/1/


class GetResultOfCurrentDay(APIView):
    def get(self, request, *args, **kwargs):
        pk_restaurant = kwargs.get('pk', None)
        if pk_restaurant is None:
            return Response({"error": "pk is required"}, status=400)

        today = timezone.now().date()
        start_of_day = datetime.combine(today, datetime.min.time())
        end_of_day = datetime.combine(today, datetime.max.time())

        queryset = Menu.objects.filter(creating_date__range=(start_of_day, end_of_day))
        #main_menu_list = MenuSerializer(queryset, many=True).data
        main_menu_list = queryset
        lst_of_restaurants = []

        restaurant_objects = Restaurant.objects.all()
        for restaurant in restaurant_objects:
            lst_of_restaurants.append({restaurant.id: {}})

        all_employees = Employee.objects.all()

        for menu in main_menu_list:
            for restaurant_id in lst_of_restaurants:
                if menu.id_restaurant == list(restaurant_id.keys())[0]:
                    #test_mass.append((menu["name"], restaurant_id, str(list(restaurant_id.keys())[0])))
                    #lst_of_restaurants[restaurant_id] = restaurant_id.get(restaurant_id, 1) + 1
                    #temp.append((restaurant_id, str(list(restaurant_id.keys())[0]), restaurant_id[list(restaurant_id.keys())[0]]))

                   for employee in all_employees:
                      if employee.vote_result == menu.id:
                        restaurant_id[list(restaurant_id.keys())[0]][menu.id] = restaurant_id[list(restaurant_id.keys())[0]].get(menu.id, 0) + 1

        total_menu_results = {}
        #for result in lst_of_restaurants:


        return Response({'rests': lst_of_restaurants})
