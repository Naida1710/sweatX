from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='reviews'),
    path('add/', views.add_review, name='add_review'),
    path('<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('<int:review_id>/comment/', views.add_review_comment, name='add_review_comment'),
    path('<int:review_id>/vote/<str:vote_type>/', views.vote_review, name='vote_review'),
    path('comment/<int:comment_id>/vote/<str:vote_type>/', views.vote_review_comment, name='vote_review_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_review_comment, name='edit_review_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_review_comment, name='delete_review_comment'),
]