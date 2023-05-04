from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('salute/<str:username>', views.hello),
]