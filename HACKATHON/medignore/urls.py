from django.urls import path
from . import views

app_name = 'medignore'

urlpatterns = [
    # path('service/', views.service, name="service"),
    #path('temp/', views.temp, name="temp"),
    # path('url/<medicine>/', views.url_parse, name="url_parse"),
    path('result/', views.result, name="result"),
    # path('result/', views.result, name="result"),
    # path('search/', views.search, name="search"),
    path('', views.search, name="search"),
    path('clear/',views.clear_database, name='clear_database'),
]