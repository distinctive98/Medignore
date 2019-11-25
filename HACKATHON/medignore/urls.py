from django.urls import path
from . import views

app_name = 'medignore'

urlpatterns = [
    path('result/', views.result, name="result"),
    path('search/', views.search, name="search"),
    path('test/', views.test, name='test'),
    path('temp/', views.temp, name="temp"),
    path('', views.main, name="main"),
    path('clear/',views.clear_database, name='clear_database'),
    # path('basic-upload/', views.BasicUploadView, name='basic_upload'),
    # path('drag-and-drop-upload/',views.DragAndDropUploadView, name='drag_and_drop_upload'),
]