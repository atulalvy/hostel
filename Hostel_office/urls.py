from django.urls import path

from . import views

app_name = 'Hostel_office'

urlpatterns = [
    path('', views.index, name='index'),
    path('getdata/', views.get_data, name="get data"),
    path('savedata/', views.save_data, name="save data"),
    path('add_dept/', views.add_dept, name="add dept"),
    path('create/', views.create, name="create"),
    path('printdata/', views.printdata, name="printdata"),
    path('control/', views.control, name='application_control'),
    path('create_department/', views.add_departments, name="create departments"),
    path('get_department/', views.get_departments, name="get departments"),
    path('create_dept/', views.create_department, name="create dept back"),
    path('delete_dept/', views.delete_department, name="delete department"),
    path('delete/', views.delete, name="delete"),
]
