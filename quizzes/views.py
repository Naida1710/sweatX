from django.shortcuts import render, redirect


QUESTIONS = [
    {
        "key": "location",
        "question": "Where do you want to train?",
        "type": "radio",
        "options": [
            ("home", "At home"),
            ("gym", "At a gym"),
        ],
    },
    {
        "key": "goal",
        "question": "Choose your goal",
        "type": "radio",
        "options": [
            ("weight_loss", "Weight loss"),
            ("wellness_longevity", "Wellness and longevity"),
            ("energy_vitality", "Energy and vitality"),
            ("balance_mobility", "Balance and mobility"),
        ],
    },
    {
        "key": "motivation",
        "question": "What else motivates you to exercise?",
        "type": "radio",
        "options": [
            ("muscle_strength", "Support muscle strength"),
            ("reduce_stress", "Reduce stress"),
            ("enhance_posture", "Enhance posture"),
        ],
    },
    {
        "key": "best_shape",
        "question": "How long ago were you in the best shape of your life?",
        "type": "radio",
        "options": [
            ("less_than_year", "Less than a year ago"),
            ("1_3_years", "1–3 years ago"),
            ("never", "Never"),
        ],
    },
    {
        "key": "flexibility",
        "question": "How flexible are you?",
        "type": "radio",
        "options": [
            ("very_flexible", "Very flexible"),
            ("pretty_flexible", "Pretty flexible"),
            ("not_good", "Not that good"),
        ],
    },
    {
        "key": "experience_level",
        "question": "Choose your experience level",
        "type": "radio",
        "options": [
            ("beginner", "Beginner (I have never trained before)"),
            ("intermediate", "Intermediate (I have trained regularly for at least one year)"),
            ("advanced", "Advanced (I have trained consistently for years and have better than average strength and muscle development)"),
        ],
    },
    {
        "key": "gender",
        "question": "Select gender",
        "type": "radio",
        "options": [
            ("male", "Male"),
            ("female", "Female"),
            ("prefer_not_to_say", "Prefer not to say"),
        ],
    },
    {
        "key": "age_range",
        "question": "Choose age range",
        "type": "radio",
        "options": [
            ("16_20", "16–20"),
            ("21_30", "21–30"),
            ("31_40", "31–40"),
            ("41_50", "41–50"),
            ("51_plus", "51+"),
        ],
    },
    {
        "key": "pushups",
        "question": "How many push-ups can you do in a single set?",
        "type": "radio",
        "options": [
            ("10_or_less", "10 or less"),
            ("11_25", "11–25"),
            ("26_40", "26–40"),
            ("41_65", "41–65"),
            ("65_plus", "More than 65"),
        ],
    },
    {
        "key": "training_focus",
        "question": "How would you like to focus your training?",
        "type": "range",
        "min": 0,
        "max": 100,
        "default": 50,
        "left_label": "Burn fat",
        "right_label": "Build muscle",
        "help_text": "Move the slider left or right to personalise your training focus.",
    },
]


def training_quiz(request):
    answers = request.session.get("quiz_answers", {})
    total_steps = len(QUESTIONS)

    try:
        step = int(request.GET.get("step", 1))
    except ValueError:
        step = 1

    if step < 1:
        step = 1
    if step > total_steps:
        step = total_steps

    current_question = QUESTIONS[step - 1]
    question_key = current_question["key"]

    if request.method == "POST":
        action = request.POST.get("action", "continue")

        if action == "back":
            previous_step = max(1, step - 1)
            return redirect(f"/quizzes/training-quiz/?step={previous_step}")

        value = request.POST.get(question_key)
        if value:
            answers[question_key] = value
            request.session["quiz_answers"] = answers

        if action == "continue":
            if step < total_steps:
                return redirect(f"/quizzes/training-quiz/?step={step + 1}")
            return redirect("quiz_result")

    context = {
        "step": step,
        "total_steps": total_steps,
        "question_data": current_question,
        "saved_value": answers.get(question_key, current_question.get("default", "")),
        "progress_percent": int((step / total_steps) * 100),
    }

    return render(request, "quizzes/training_quiz.html", context)


def quiz_result(request):
    answers = request.session.get("quiz_answers", {})

    if not answers:
        return redirect("training_quiz")

    beginner_score = 0
    intermediate_score = 0
    advanced_score = 0

    experience_level = answers.get("experience_level")
    pushups = answers.get("pushups")
    best_shape = answers.get("best_shape")
    flexibility = answers.get("flexibility")
    location = answers.get("location")
    training_focus = int(answers.get("training_focus", 50))

    if experience_level == "beginner":
        beginner_score += 3
    elif experience_level == "intermediate":
        intermediate_score += 3
    elif experience_level == "advanced":
        advanced_score += 3

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

    if best_shape == "never":
        beginner_score += 2
    elif best_shape == "1_3_years":
        intermediate_score += 1
    elif best_shape == "less_than_year":
        advanced_score += 1

    if flexibility == "not_good":
        beginner_score += 1
    elif flexibility == "pretty_flexible":
        intermediate_score += 1
    elif flexibility == "very_flexible":
        advanced_score += 1

    if location == "home":
        beginner_score += 1
    elif location == "gym":
        intermediate_score += 1
        advanced_score += 1

    result_level = "Beginner"
    if advanced_score > intermediate_score and advanced_score > beginner_score:
        result_level = "Advanced"
    elif intermediate_score > beginner_score:
        result_level = "Intermediate"

    goal_labels = {
        "weight_loss": "Weight loss",
        "wellness_longevity": "Wellness and longevity",
        "energy_vitality": "Energy and vitality",
        "balance_mobility": "Balance and mobility",
    }

    motivation_labels = {
        "muscle_strength": "Support muscle strength",
        "reduce_stress": "Reduce stress",
        "enhance_posture": "Enhance posture",
    }

    location_labels = {
        "home": "At home",
        "gym": "At a gym",
    }

    context = {
        "result_level": result_level,
        "goal": goal_labels.get(answers.get("goal"), ""),
        "motivation": motivation_labels.get(answers.get("motivation"), ""),
        "location": location_labels.get(answers.get("location"), ""),
        "training_focus": training_focus,
    }

    return render(request, "quizzes/result.html", context)