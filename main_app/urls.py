from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.about, name='about'),
    path('restaurants/', views.restaurants_index, name='index'),
    path('restaurants/<int:r_id>/', views.restaurants_detail, name='detail'),
    # create form 1 - deliver a form
    path('restaurants/create_form', views.create_form),
    # create step 2 - accept form submission    
    path('restaurants/submit_create_form',views.submit_create_form),
]

