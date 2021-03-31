from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
# Add the following import
from django.http import HttpResponse

def create_form(request):
  return render(request,'create_form.html')
# create part 2 - handle the form submission 
def submit_create_form(request):
  # put form data in database 
  Restaurant.objects.create(
    name = request.POST['name'],
    age=request.POST['age'],
    cuisine=request.POST['cuisine'],
    capacity=request.POST['capacity'],
  )
  return redirect('/restaurants')

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