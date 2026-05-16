from django.shortcuts import render, redirect


QUESTIONS = [
    {
        "key": "primary_goal",
        "question": "What is your primary goal?",
        "type": "radio",
        "options": [
            ("build_strength", "Build strength and muscle"),
            ("run_further", "Run further and improve endurance"),
            ("get_started", "Get started with fitness in general"),
            ("lose_weight", "Lose weight"),
        ],
    },
    {
        "key": "experience",
        "question": "How would you describe your fitness experience?",
        "type": "radio",
        "options": [
            ("never_or_starting", "Never trained or just starting out"),
            ("on_and_off", "Some experience, on and off"),
            ("one_two_years", "Trained consistently for 1-2 years"),
            ("three_plus", "3+ years of consistent training"),
        ],
    },
    {
        "key": "training_location",
        "question": "Where do you prefer to train?",
        "type": "radio",
        "options": [
            ("home", "At home"),
            ("gym", "At a gym"),
            ("outdoors", "Outdoors"),
            ("mix", "A mix of all"),
        ],
    },
    {
        "key": "time_per_week",
        "question": "How much time can you dedicate per week?",
        "type": "radio",
        "options": [
            ("1_3", "1-3 hours (just starting)"),
            ("3_5", "3-5 hours"),
            ("5_8", "5-8 hours"),
            ("8_plus", "8+ hours (very committed)"),
        ],
    },
    {
        "key": "cardio_baseline",
        "question": "What does your current cardio look like?",
        "type": "radio",
        "options": [
            ("winded_stairs", "I get winded climbing stairs"),
            ("walk_30min", "I can walk 30 minutes comfortably"),
            ("run_occasional", "I run or cycle occasionally"),
            ("run_regular", "I run regularly (10+ km per week)"),
        ],
    },
    {
        "key": "pushups",
        "question": "How many push-ups can you do in one set?",
        "type": "radio",
        "options": [
            ("0_5", "0-5"),
            ("6_15", "6-15"),
            ("16_30", "16-30"),
            ("30_plus", "More than 30"),
        ],
    },
    {
        "key": "program_history",
        "question": "Have you completed a structured workout program before?",
        "type": "radio",
        "options": [
            ("never", "Never"),
            ("started_quit", "Started one but didn't finish"),
            ("one_two", "Yes, one or two"),
            ("several", "Yes, several"),
        ],
    },
    {
        "key": "equipment",
        "question": "What equipment do you have access to?",
        "type": "radio",
        "options": [
            ("body_only", "Just my body and a mat"),
            ("some_weights", "Some dumbbells or resistance bands"),
            ("home_gym", "Full home gym"),
            ("commercial_gym", "Commercial gym"),
        ],
    },
    {
        "key": "running_ability",
        "question": "How would you rate your running ability?",
        "type": "radio",
        "options": [
            ("cant_run", "I can't run more than a minute"),
            ("jog_short", "I can jog for 10-15 minutes"),
            ("run_5k", "I can run a 5K comfortably"),
            ("run_10k_plus", "I can run 10K or more"),
        ],
    },
    {
        "key": "training_time",
        "question": "When do you train best?",
        "type": "radio",
        "options": [
            ("morning", "Early morning"),
            ("lunch", "Lunch break"),
            ("evening", "Evening"),
            ("night", "Late night"),
        ],
    },
    {
        "key": "motivation",
        "question": "How would you describe your motivation?",
        "type": "radio",
        "options": [
            ("need_structure", "I need a structured plan to stick with it"),
            ("get_stronger", "I want to get visibly stronger"),
            ("race_event", "I have a race or event coming up"),
            ("feel_healthier", "I want to feel healthier overall"),
        ],
    },
    {
        "key": "appeal",
        "question": "Which sounds more appealing right now?",
        "type": "radio",
        "options": [
            ("build_muscle", "Building visible muscle and feeling stronger"),
            ("finish_line", "Crossing a finish line and proving endurance"),
            ("build_habit", "Building a consistent habit and feeling better"),
        ],
    },
    {
        "key": "current_state",
        "question": "Do you currently experience any of these?",
        "type": "radio",
        "options": [
            ("joint_pain", "Joint pain or recovery issues"),
            ("inconsistent", "Difficulty staying consistent"),
            ("injury_free", "I'm injury-free and feel great"),
            ("plateau", "I plateau easily"),
        ],
    },
    {
        "key": "progress_priority",
        "question": "How important is rapid visible progress?",
        "type": "radio",
        "options": [
            ("very_important", "Very important - I want to see results fast"),
            ("patient", "Somewhat important - I'm patient"),
            ("long_term", "I prioritize long-term health"),
            ("just_starting", "I'm just here to start"),
        ],
    },
    {
        "key": "biggest_barrier",
        "question": "What's your biggest barrier to training?",
        "type": "radio",
        "options": [
            ("dont_know_start", "I don't know where to start"),
            ("get_bored", "I get bored easily"),
            ("no_time", "I don't have time"),
            ("just_need_plan", "Nothing - I just need a plan"),
        ],
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
    from products.models import Product
    from django.contrib import messages

    answers = request.session.get("quiz_answers", {})

    if not answers:
        return redirect("training_quiz")

    beginner_score = 0
    strength_score = 0
    marathon_score = 0

    scoring = {
        "primary_goal": {
            "build_strength": (0, 5, 0),
            "run_further": (0, 0, 5),
            "get_started": (5, 0, 0),
            "lose_weight": (1, 1, 0),
        },
        "experience": {
            "never_or_starting": (3, 0, 0),
            "on_and_off": (2, 0, 0),
            "one_two_years": (0, 2, 1),
            "three_plus": (0, 3, 2),
        },
        "training_location": {
            "home": (2, 0, 0),
            "gym": (0, 2, 0),
            "outdoors": (0, 0, 2),
            "mix": (1, 1, 1),
        },
        "time_per_week": {
            "1_3": (2, 0, 0),
            "3_5": (1, 1, 0),
            "5_8": (0, 2, 0),
            "8_plus": (0, 0, 2),
        },
        "cardio_baseline": {
            "winded_stairs": (2, 0, 0),
            "walk_30min": (1, 1, 0),
            "run_occasional": (0, 0, 2),
            "run_regular": (0, 0, 3),
        },
        "pushups": {
            "0_5": (3, 0, 0),
            "6_15": (2, 1, 0),
            "16_30": (0, 2, 0),
            "30_plus": (0, 2, 0),
        },
        "program_history": {
            "never": (2, 0, 0),
            "started_quit": (1, 0, 0),
            "one_two": (0, 1, 1),
            "several": (0, 2, 1),
        },
        "equipment": {
            "body_only": (3, 0, 0),
            "some_weights": (2, 1, 0),
            "home_gym": (0, 2, 0),
            "commercial_gym": (0, 3, 0),
        },
        "running_ability": {
            "cant_run": (2, 0, 0),
            "jog_short": (0, 0, 1),
            "run_5k": (0, 0, 2),
            "run_10k_plus": (0, 0, 3),
        },
        "training_time": {
            "morning": (1, 1, 1),
            "lunch": (1, 1, 1),
            "evening": (1, 1, 1),
            "night": (1, 1, 1),
        },
        "motivation": {
            "need_structure": (2, 0, 0),
            "get_stronger": (0, 2, 0),
            "race_event": (0, 0, 3),
            "feel_healthier": (1, 1, 1),
        },
        "appeal": {
            "build_muscle": (0, 3, 0),
            "finish_line": (0, 0, 3),
            "build_habit": (3, 0, 0),
        },
        "current_state": {
            "joint_pain": (2, 0, 0),
            "inconsistent": (1, 0, 0),
            "injury_free": (0, 1, 1),
            "plateau": (0, 1, 0),
        },
        "progress_priority": {
            "very_important": (0, 2, 0),
            "patient": (1, 1, 1),
            "long_term": (0, 0, 2),
            "just_starting": (2, 0, 0),
        },
        "biggest_barrier": {
            "dont_know_start": (3, 0, 0),
            "get_bored": (0, 0, 1),
            "no_time": (1, 0, 0),
            "just_need_plan": (1, 1, 1),
        },
    }

    for key, value in answers.items():
        if key in scoring and value in scoring[key]:
            b, s, m = scoring[key][value]
            beginner_score += b
            strength_score += s
            marathon_score += m

    program_name_map = {
        "beginner": "Beginner Home Workout Plan",
        "strength": "12-Week Strength Program (PDF)",
        "marathon": "Marathon Training 16 Weeks",
    }

    program_blurbs = {
        "beginner": "Based on your answers, you're ready to build a strong foundation. This 8-week home program is designed for people just starting out, using bodyweight movements that progress at your pace.",
        "strength": "Your answers show you're ready to push harder. This 12-week strength program is built for people who want visible muscle and measurable strength gains.",
        "marathon": "You're built for endurance. This 16-week marathon training plan will guide you from where you are now to crossing the finish line with confidence.",
    }

    scores = {
        "beginner": beginner_score,
        "strength": strength_score,
        "marathon": marathon_score,
    }
    winner_key = max(scores, key=scores.get)
    winner_name = program_name_map[winner_key]
    winner_blurb = program_blurbs[winner_key]

    try:
        product = Product.objects.get(name=winner_name)
    except Product.DoesNotExist:
        messages.error(request, "We had trouble loading your recommended program. Please browse our programs directly.")
        return redirect("products")

    context = {
        "product": product,
        "blurb": winner_blurb,
        "scores": scores,
    }

    return render(request, "quizzes/result.html", context)