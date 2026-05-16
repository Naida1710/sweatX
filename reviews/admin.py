from django.contrib import admin
from .models import Review, ReviewComment, ReviewVote, ReviewCommentVote


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rating', 'approved', 'created_at')
    list_filter = ('rating', 'approved', 'created_at')
    search_fields = ('title', 'comment', 'user__username')


@admin.register(ReviewComment)
class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'approved', 'created_at')
    list_filter = ('approved', 'created_at')
    search_fields = ('comment', 'user__username', 'review__title')


@admin.register(ReviewVote)
class ReviewVoteAdmin(admin.ModelAdmin):
    list_display = ('review', 'user', 'vote_type', 'created_at')
    list_filter = ('vote_type', 'created_at')


@admin.register(ReviewCommentVote)
class ReviewCommentVoteAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'vote_type', 'created_at')
    list_filter = ('vote_type', 'created_at')
