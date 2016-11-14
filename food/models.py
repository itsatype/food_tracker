from __future__ import unicode_literals

from django.db import models

class Food(models.Model):
  food_item = models.CharField(max_length=200)
  upc = models.CharField(max_length=25)
  image = models.CharField(max_length=200)
  brand = models.CharField(max_length=200)
  credits = models.IntegerField()

class Company(models.Model):
   name = models.CharField(max_length=200)


class User(models.Model):
  name = models.CharField(max_length=200)
  pin = models.IntegerField(max_length=4)   
  company =  models.ForeignKey(Company, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name
   
class Order(models.Model):
  user =  models.ForeignKey(User, on_delete=models.CASCADE)
  food = models.ForeignKey(Food, on_delete=models.CASCADE)
  quantity = models.IntegerField(max_length=3)
