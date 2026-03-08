from django.urls import path
from . import views

urlpatterns = [
    path("training-quiz/", views.training_quiz, name="training_quiz"),
    path("beginner/", views.beginner_quiz, name="beginner_quiz"),
    path("intermediate/", views.intermediate_quiz, name="intermediate_quiz"),
    path("advanced/", views.advanced_quiz, name="advanced_quiz"),
    path("choose-plans/", views.choose_plans, name="choose_plans"),
    path("programs/", views.all_programs, name="all_programs"),
]
