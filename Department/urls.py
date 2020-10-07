from django.urls import path

from . import views

app_name = 'Departments'

urlpatterns = [
    path('', views.index, name='index'),
    path('getdata/', views.get_data, name="get data"),
    path('savedata/', views.save_data, name="save data"),
    path('priority/', views.priority, name='priority'),


]
