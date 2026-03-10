from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from .forms import NewsletterForm
from .models import NewsletterSubscriber


def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email'].lower().strip()
            quiz_answers = request.session.get('quiz_answers', {})
            selected_goal = quiz_answers.get('goal', '')

            subscriber, created = NewsletterSubscriber.objects.get_or_create(
                email=email,
                defaults={
                    'goal': selected_goal,
                    'wants_starter_plan': True,
                }
            )

            if not created:
                subscriber.goal = subscriber.goal or selected_goal
                subscriber.wants_starter_plan = True
                subscriber.save()

            return redirect(f"{reverse('home')}?subscribed=1")

        messages.error(request, 'Please enter a valid email address.')
        return redirect(reverse('home'))

    return redirect(reverse('home'))