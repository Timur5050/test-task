from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name_restaurant = models.CharField(max_length=255)
    menu_update_time = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    id_restaurant = models.IntegerField(null=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    vote_result = models.IntegerField(null=True)


class Menu(models.Model):
    id_restaurant = models.IntegerField(null=True)
    creating_date = models.DateTimeField(auto_now_add=True)
    menu_items = models.JSONField()
