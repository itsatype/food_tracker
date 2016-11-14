from django.shortcuts import render
from django.http import HttpResponse

from .models import Food


def index(request):
  return HttpResponse("Hello, Eli")


def new(request):
  food = Food()
  return render(request, 'food/new.html')

def create(request):
  return HttpResponse(request.POST['food_item'])

