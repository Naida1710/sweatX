from django.contrib import messages
from django.shortcuts import redirect
from .forms import NewsletterForm
from .models import NewsletterSubscriber


def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email'].lower().strip()

            if NewsletterSubscriber.objects.filter(email=email).exists():
                messages.warning(request, 'This email is already subscribed.')
            else:
                NewsletterSubscriber.objects.create(email=email)
                messages.success(request, 'You have successfully subscribed to the sweatX newsletter!')

        else:
            messages.error(request, 'Please enter a valid email address.')

    return redirect(request.META.get('HTTP_REFERER', 'home'))