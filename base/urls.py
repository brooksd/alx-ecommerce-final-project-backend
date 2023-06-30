from django.urls import path
from . import views 

urlPattern = [
    path('', views.getRoutes, name='routes'),
]