from django.urls import path

from . import views

app_name = "Homapage"
urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('details/', views.details, name='details'),
    path('instructions/', views.instructions, name='instructions'),
    path('details/', views.details, name='details')
]
