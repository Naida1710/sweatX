from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('starter-plan/', views.starter_plan, name='starter_plan'),
]
