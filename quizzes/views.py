from django.shortcuts import render


def training_quiz(request):
    if request.method == "POST":
        location = request.POST.get("location")
        goal = request.POST.get("goal")
        motivation = request.POST.get("motivation")
        best_shape = request.POST.get("best_shape")
        flexibility = request.POST.get("flexibility")
        experience_level = request.POST.get("experience_level")
        gender = request.POST.get("gender")
        age_range = request.POST.get("age_range")
        pushups = request.POST.get("pushups")
        training_focus = request.POST.get("training_focus")

        beginner_score = 0
        intermediate_score = 0
        advanced_score = 0

        # Experience level scoring
        if experience_level == "beginner":
            beginner_score += 3
        elif experience_level == "intermediate":
            intermediate_score += 3
        elif experience_level == "advanced":
            advanced_score += 3

        # Push-up scoring
        if pushups == "10_or_less":
            beginner_score += 2
        elif pushups == "11_25":
            beginner_score += 1
            intermediate_score += 1
        elif pushups == "26_40":
            intermediate_score += 2
        elif pushups == "41_65":
            advanced_score += 2
        elif pushups == "65_plus":
            advanced_score += 3

        # Best shape scoring
        if best_shape == "never":
            beginner_score += 2
        elif best_shape == "1_3_years":
            intermediate_score += 1
        elif best_shape == "less_than_year":
            advanced_score += 1

        # Flexibility scoring
        if flexibility == "not_good":
            beginner_score += 1
        elif flexibility == "pretty_flexible":
            intermediate_score += 1
        elif flexibility == "very_flexible":
            advanced_score += 1

        # Training location scoring
        if location == "home":
            beginner_score += 1
        elif location == "gym":
            intermediate_score += 1
            advanced_score += 1

        # Training focus slider
        focus_value = int(training_focus) if training_focus else 50

        result_level = "Beginner"
        if advanced_score >= intermediate_score and advanced_score >= beginner_score:
            result_level = "Advanced"
        elif intermediate_score >= beginner_score:
            result_level = "Intermediate"

        context = {
            "result_level": result_level,
            "location": location,
            "goal": goal,
            "motivation": motivation,
            "gender": gender,
            "age_range": age_range,
            "training_focus": focus_value,
        }

        return render(request, "quizzes/result.html", context)

    return render(request, "quizzes/training_quiz.html")


def beginner_quiz(request):
    return render(request, "quizzes/beginner.html")


def intermediate_quiz(request):
    return render(request, "quizzes/intermediate.html")


def advanced_quiz(request):
    return render(request, "quizzes/advanced.html")