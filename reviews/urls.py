from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='reviews'),
    path('add/', views.add_review, name='add_review'),
    path('<int:review_id>/comment/', views.add_review_comment, name='add_review_comment'),
]