from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import StarterPlanProgress


def index(request):
    quiz_answers = request.session.get('quiz_answers', {})
    selected_goal = quiz_answers.get('goal')

    homepage_content = {
        'headline': 'Find your perfect fitness path',
        'subheadline': 'Shop supplements, discover training plans, and build your sweatX journey.',
        'cta_text': 'Discover my plan',
        'cta_url': '/quizzes/training-quiz/',
    }

    goal_content = {
        'weight_loss': {
            'headline': 'Your weight loss journey starts here',
            'subheadline': 'Discover products and routines designed to help you stay consistent and feel stronger.',
            'cta_text': 'Shop weight loss support',
            'cta_url': '/products/',
        },
        'wellness_longevity': {
            'headline': 'Build long-term wellness with sweatX',
            'subheadline': 'Support your daily health with smarter routines, recovery, and nutrition.',
            'cta_text': 'Explore wellness essentials',
            'cta_url': '/products/',
        },
        'energy_vitality': {
            'headline': 'Boost your energy and vitality',
            'subheadline': 'Find products and plans that help you feel sharper, stronger, and more active.',
            'cta_text': 'Shop for energy',
            'cta_url': '/products/',
        },
        'balance_mobility': {
            'headline': 'Move better and feel stronger',
            'subheadline': 'Improve flexibility, balance, and control with the right support.',
            'cta_text': 'Explore mobility support',
            'cta_url': '/products/',
        },
    }

    if selected_goal in goal_content:
        homepage_content = goal_content[selected_goal]

    context = {
        'selected_goal': selected_goal,
        'homepage_content': homepage_content,
    }
    return render(request, 'home/index.html', context)


def about(request):
    """ A view to return the about us page """
    return render(request, 'home/about.html')


def starter_plan(request):
    quiz_answers = request.session.get('quiz_answers', {})
    selected_goal = quiz_answers.get('goal')

    completed_steps = []
    if request.user.is_authenticated:
        completed_steps = list(
            StarterPlanProgress.objects.filter(user=request.user).values_list('step_number', flat=True)
        )

    context = {
        'selected_goal': selected_goal,
        'completed_steps': completed_steps,
    }
    return render(request, 'home/starter_plan.html', context)


@require_POST
@login_required
def complete_starter_step(request, step_number):
    """ Mark a starter plan step as complete for the logged-in user """
    if step_number < 1 or step_number > 7:
        return JsonResponse({'error': 'Invalid step number'}, status=400)

    StarterPlanProgress.objects.get_or_create(
        user=request.user,
        step_number=step_number,
    )

    completed_steps = list(
        StarterPlanProgress.objects.filter(user=request.user).values_list('step_number', flat=True)
    )

    return JsonResponse({
        'success': True,
        'completed_steps': completed_steps,
    })


def handler404(request, exception):
    return render(request, '404.html', status=404)

