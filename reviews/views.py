from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .forms import ReviewForm, ReviewCommentForm
from .models import Review, ReviewComment, ReviewVote, ReviewCommentVote


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

@login_required
def vote_review(request, review_id, vote_type):
    review = get_object_or_404(Review, id=review_id, approved=True)

    if vote_type not in ['like', 'dislike']:
        messages.error(request, 'Invalid vote.')
        return redirect('reviews')

    vote, created = ReviewVote.objects.get_or_create(
        review=review,
        user=request.user,
        defaults={'vote_type': vote_type}
    )

    if not created:
        vote.vote_type = vote_type
        vote.save()

    return redirect('reviews')


@login_required
def vote_review_comment(request, comment_id, vote_type):
    comment = get_object_or_404(ReviewComment, id=comment_id, approved=True)

    if vote_type not in ['like', 'dislike']:
        messages.error(request, 'Invalid vote.')
        return redirect('reviews')

    vote, created = ReviewCommentVote.objects.get_or_create(
        comment=comment,
        user=request.user,
        defaults={'vote_type': vote_type}
    )

    if not created:
        vote.vote_type = vote_type
        vote.save()

    return redirect('reviews')

@login_required
def edit_review_comment(request, comment_id):
    review_comment = get_object_or_404(ReviewComment, id=comment_id)

    if review_comment.user != request.user:
        messages.error(request, "You can only edit your own comments.")
        return redirect('reviews')

    if request.method == 'POST':
        updated_comment = request.POST.get('comment')

        if updated_comment and updated_comment.strip():
            review_comment.comment = updated_comment.strip()
            review_comment.save()
            messages.success(request, 'Your comment has been updated.')
        else:
            messages.error(request, 'Comment cannot be empty.')

    return redirect('reviews')


@login_required
def delete_review_comment(request, comment_id):
    review_comment = get_object_or_404(ReviewComment, id=comment_id)

    if review_comment.user != request.user:
        messages.error(request, "You can only delete your own comments.")
        return redirect('reviews')

    if request.method == 'POST':
        review_comment.delete()
        messages.success(request, 'Your comment has been deleted.')

    return redirect('reviews')