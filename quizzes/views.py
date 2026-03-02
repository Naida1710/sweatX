from django.shortcuts import render, redirect

def training_quiz(request):
    if request.method == "POST":

        score = 0

        experience = request.POST.get("experience")
        pushups = request.POST.get("pushups")

        # Question 1 scoring
        if experience == "0-6":
            score += 1
        elif experience == "6-24":
            score += 2
        elif experience == "24+":
            score += 3

        # Question 2 scoring
        if pushups == "low":
            score += 1
        elif pushups == "medium":
            score += 2
        elif pushups == "high":
            score += 3

        # Decide level
        if score <= 3:
            return redirect("beginner_quiz")
        elif score <= 5:
            return redirect("intermediate_quiz")
        else:
            return redirect("advanced_quiz")

    return render(request, "quizzes/training_quiz.html")


def beginner_quiz(request):
    return render(request, "quizzes/beginner.html")

def intermediate_quiz(request):
    return render(request, "quizzes/intermediate.html")

def advanced_quiz(request):
    return render(request, "quizzes/advanced.html")

