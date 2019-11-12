from django.urls import path
from . import views

app_name = 'medignore'

urlpatterns = [
    path('result/', views.result, name="result"),
    path('search/', views.search, name="search"),
    path('temp/', views.temp, name="temp"),
    path('', views.main, name="main"),
]