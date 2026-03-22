from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_list, name='film_list'),
    path('add/', views.add_film, name='add_film'),
    path('film/<int:pk>/', views.film_detail, name='film_detail'),
]