from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Restaurant, Employee, Menu


class RestaurantSerializer(serializers.Serializer):
    name_restaurant = serializers.CharField(max_length=255)
    menu_update_time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)

    #def update(self, instance, validated_data):


class EmployeeSerializer(serializers.Serializer):
    id_restaurant = serializers.IntegerField(default=0)
    name = serializers.CharField(max_length=255, default='no')
    surname = serializers.CharField(max_length=255, default='name')
    vote_result = serializers.IntegerField()

    def validate(self, data):
        id_restaurant = data.get('id_restaurant')
        vote_result = data.get('vote_result')

        if id_restaurant != Menu.objects.filter(id=vote_result).first().id_restaurant:
            raise serializers.ValidationError("Invalid vote result for the specified restaurant.")

        return data

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.vote_result = validated_data.get("vote_result", instance.vote_result)
        instance.save()
        return instance


class MenuSerializer(serializers.Serializer):
    name = serializers.CharField()
    id_restaurant = serializers.IntegerField()
    creating_date = serializers.DateTimeField(read_only=True)
    menu_items = serializers.JSONField()

    def create(self, validated_data):
        return Menu.objects.create(**validated_data)




