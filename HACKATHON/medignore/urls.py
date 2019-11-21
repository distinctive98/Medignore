from django.urls import path
from . import views

app_name = 'medignore'

urlpatterns = [
    path('test/', views.test, name='test'),
    # path('temp/', views.temp, name="temp"),
    path('', views.main, name="main"),
    path('clear/',views.clear_database, name='clear_database'),
    path('result/', views.result, name ='result'),
]