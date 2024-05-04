import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Restaurant


class RestaurantSerializer(serializers.Serializer):
    id_restaurant = serializers.IntegerField()
    name_restaurant = serializers.CharField(max_length=255)
    menu_update_time = serializers.DateTimeField(read_only=True)

