from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('starter-plan/', views.starter_plan, name='starter_plan'),
    path('starter-plan/complete/<int:step_number>/', views.complete_starter_step, name='complete_starter_step'),
]
