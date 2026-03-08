from django.shortcuts import render, redirect


def choose_plans(request):
    return render(request, "quizzes/choose_plans.html")


def training_quiz(request):
    if request.method == "POST":
        location = request.POST.get("location")

        if location == "home":
            return redirect("beginner_quiz")
        elif location == "gym":
            return redirect("intermediate_quiz")

    return render(request, "quizzes/training_quiz.html")


def beginner_quiz(request):
    return render(request, "quizzes/beginner.html")


def intermediate_quiz(request):
    return render(request, "quizzes/intermediate.html")


def advanced_quiz(request):
    return render(request, "quizzes/advanced.html")