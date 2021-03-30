from django.shortcuts import render
from .models import Restaurant

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Add the Restaurants class & list and view function below the imports
# class Restaurant:  # Note that parens are optional if not inheriting from another class
  # def __init__(self, name, cuisine, description, capacity):
  #   self.name = name
  #   self.cuisine = cuisine
  #   self.description = description
  #   self.capacity = capacity

# restaurants = [
#   Restaurant('Best Japanese Noodles', 'Ramen', 'Patio only', 50),
#   Restaurant('Kimchi FTW', 'Korean', 'Very spicy food', 100),
#   Restaurant('Asian Sensation', 'Chinese', 'Quick service', 20)
# ]

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def restaurants_index(request):
    restaurants = Restaurant.objects.all()
    return render(request,'restaurants/index.html',{'restaurants': restaurants})

def restaurants_detail(request, r_id):
  r = Restaurant.objects.get(id=r_id)
  return render(request, 'restaurants/detail.html', { 'r': r })