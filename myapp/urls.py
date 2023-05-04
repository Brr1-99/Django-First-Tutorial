from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('salute/<str:username>', views.hello),
    path('subjects', views.subject),
    path('subject/<str:name>', views.subject_or_404),
]