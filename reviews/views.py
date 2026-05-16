from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ReviewCommentForm, ReviewForm
from .models import Review, ReviewComment, ReviewVote, ReviewCommentVote


def review_list(request):
    """
    Public review page:
    - Anyone can see approved reviews
    - Tracks likes for both reviews and comments to toggle red hearts
    """
    reviews = Review.objects.filter(approved=True)
    user_liked_reviews = []
    user_liked_comments = []

    if request.user.is_authenticated:
        # Get IDs of reviews the user liked
        user_liked_reviews = ReviewVote.objects.filter(
            user=request.user,
            vote_type='like'
        ).values_list('review_id', flat=True)

        # Get IDs of comments the user liked
        user_liked_comments = ReviewCommentVote.objects.filter(
            user=request.user,
            vote_type='like'
        ).values_list('comment_id', flat=True)

    context = {
        'reviews': reviews,
        'form': ReviewForm() if request.user.is_authenticated else None,
        'comment_form': (
            ReviewCommentForm() if request.user.is_authenticated else None
        ),
        'user_liked_reviews': user_liked_reviews,
        'user_liked_comments': user_liked_comments,  # Added this
    }
    return render(request, 'reviews/review_list.html', context)


@login_required
@require_POST
def add_review(request):
    form = ReviewForm(request.POST, request.FILES)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.save()
        messages.success(request, 'Thanks! Your review has been submitted.')
    return redirect('reviews')


@login_required
@require_POST
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user != request.user:
        messages.error(request, 'You can only edit your own review.')
        return redirect('reviews')

    form = ReviewForm(request.POST, request.FILES, instance=review)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your review has been updated.')
    return redirect('reviews')


@login_required
@require_POST
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user == request.user:
        review.delete()
        messages.success(request, 'Your review has been deleted.')
    return redirect('reviews')


@login_required
@require_POST
def add_review_comment(request, review_id):
    review = get_object_or_404(Review, id=review_id, approved=True)
    form = ReviewCommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        messages.success(request, 'Your comment has been added.')
    return redirect('reviews')


@login_required
@require_POST
def vote_review(request, review_id, vote_type):
    """Handles liking/disliking the main post"""
    review = get_object_or_404(Review, id=review_id, approved=True)
    vote, created = ReviewVote.objects.get_or_create(
        review=review,
        user=request.user,
        defaults={'vote_type': vote_type}
    )
    if not created:
        if vote.vote_type == vote_type:
            vote.delete()
        else:
            vote.vote_type = vote_type
            vote.save()
    return redirect('reviews')


@login_required
@require_POST
def vote_review_comment(request, comment_id, vote_type):
    """THE MISSING FUNCTION: Handles liking/disliking comments"""
    comment = get_object_or_404(ReviewComment, id=comment_id, approved=True)
    vote, created = ReviewCommentVote.objects.get_or_create(
        comment=comment,
        user=request.user,
        defaults={'vote_type': vote_type}
    )
    if not created:
        if vote.vote_type == vote_type:
            vote.delete()
        else:
            vote.vote_type = vote_type
            vote.save()
    return redirect('reviews')


@login_required
@require_POST
def edit_review_comment(request, comment_id):
    comment = get_object_or_404(ReviewComment, id=comment_id)
    if comment.user == request.user:
        text = request.POST.get('comment', '').strip()
        if text:
            comment.comment = text
            comment.save()
            messages.success(request, 'Comment updated.')
    return redirect('reviews')


@login_required
@require_POST
def delete_review_comment(request, comment_id):
    comment = get_object_or_404(ReviewComment, id=comment_id)
    if comment.user == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted.')
    return redirect('reviews')
