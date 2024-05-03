from django.db import models

# Create your models here.


class Restaurant(models.Model):
    id_restaurant = models.IntegerField()
    name_restaurant = models.CharField(max_length=255)
    menu_update_time = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    id_restaurant = models.ForeignKey('Restaurant', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    vote_result = models.BooleanField(default=False)


class Menu(models.Model):
    id_restaurant = models.ForeignKey('Restaurant', on_delete=models.DO_NOTHING)
    creating_date = models.DateTimeField(auto_now_add=True)
    menu_items = models.JSONField()
