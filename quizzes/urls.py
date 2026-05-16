from django.urls import path
from . import views

urlpatterns = [
    path("training-quiz/", views.training_quiz, name="training_quiz"),
    path("quiz-result/", views.quiz_result, name="quiz_result"),
]
