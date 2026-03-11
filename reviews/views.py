from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReviewForm, ReviewCommentForm
from .models import Review


def review_list(request):
    reviews = Review.objects.filter(approved=True)
    review_form = ReviewForm()
    comment_form = ReviewCommentForm()

    context = {
        'reviews': reviews,
        'form': review_form,
        'comment_form': comment_form,
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


@login_required
def add_review_comment(request, review_id):
    review = get_object_or_404(Review, id=review_id, approved=True)

    if request.method == 'POST':
        form = ReviewCommentForm(request.POST)

        if form.is_valid():
            review_comment = form.save(commit=False)
            review_comment.review = review
            review_comment.user = request.user
            review_comment.save()
            messages.success(request, 'Your comment has been added.')
        else:
            messages.error(request, 'Please write a valid comment.')

    return redirect('reviews')