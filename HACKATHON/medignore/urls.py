from django.urls import path
from . import views

app_name = 'medignore'

urlpatterns = [
    path('service/', views.service, name="service"),
    path('temp/', views.temp, name="temp"),
    path('', views.main, name="main"),
]