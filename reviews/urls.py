from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='reviews'),
    path('add/', views.add_review, name='add_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
    
    # These are the missing patterns causing your error:
    path('vote/<int:review_id>/<str:vote_type>/', views.vote_review, name='vote_review'),
    path('comment/vote/<int:comment_id>/<str:vote_type>/', views.vote_review_comment, name='vote_review_comment'),
    
    # Other comment paths
    path('comment/add/<int:review_id>/', views.add_review_comment, name='add_review_comment'),
    path('comment/edit/<int:comment_id>/', views.edit_review_comment, name='edit_review_comment'),
    path('comment/delete/<int:comment_id>/', views.delete_review_comment, name='delete_review_comment'),
]