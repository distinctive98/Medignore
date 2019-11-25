from django.urls import path
from . import views

app_name = 'medignore'

urlpatterns = [
    path('url/<medicine>/', views.url_parse, name="url_parse"),
    path('result/', views.result, name="result"),
    path('search/', views.search, name="search"),
    path('test/', views.test, name='test'),
    path('', views.main, name="main"),
    path('clear/',views.clear_database, name='clear_database'),
]