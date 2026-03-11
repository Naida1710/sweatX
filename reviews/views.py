from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import ReviewForm
from .models import Review


def review_list(request):
    reviews = Review.objects.filter(approved=True)
    form = ReviewForm()

    context = {
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'reviews/review_list.html', context)


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Thanks! Your review has been submitted.')
        else:
            messages.error(request, 'Please correct the form and try again.')

    return redirect('reviews')