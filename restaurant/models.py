from django.db import models

# Create your models here.


class Restaurant(models.Model):
    name_restaurant = models.CharField(max_length=255)
    menu_update_time = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    id_restaurant = models.IntegerField(blank=True, default=0)
    #id_restaurant = models.ForeignKey("Restaurant", db_column='id_restaurant', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, default='no')
    surname = models.CharField(max_length=255, blank=True, default='name')
    vote_result = models.IntegerField(blank=True, default=0)


class Menu(models.Model):
    name = models.CharField(max_length=255, blank=True, default='standard')
    id_restaurant = models.IntegerField(null=True)
    creating_date = models.DateTimeField(auto_now_add=True)
    menu_items = models.JSONField()
