from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    title = models.CharField(max_length=100)
    comment = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    image = models.ImageField(
        upload_to='review_images/', blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    def total_likes(self):
        return self.votes.filter(vote_type='like').count()

    def total_dislikes(self):
        return self.votes.filter(vote_type='dislike').count()


class ReviewComment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='review_comments'
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.user.username} on {self.review.title}"

    def total_likes(self):
        return self.votes.filter(vote_type='like').count()

    def total_dislikes(self):
        return self.votes.filter(vote_type='dislike').count()


class ReviewVote(models.Model):
    VOTE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='votes'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='review_votes'
    )
    vote_type = models.CharField(max_length=10, choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('review', 'user')

    def __str__(self):
        return f"{self.user.username} - {self.vote_type} - {self.review.title}"


class ReviewCommentVote(models.Model):
    VOTE_CHOICES = [
        ('like', 'Like'),
        ('dislike', 'Dislike'),
    ]

    comment = models.ForeignKey(
        ReviewComment, on_delete=models.CASCADE, related_name='votes'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='review_comment_votes'
    )
    vote_type = models.CharField(max_length=10, choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('comment', 'user')

    def __str__(self):
        return (
            f"{self.user.username} - {self.vote_type} "
            f"- comment {self.comment.id}"
        )
