from django.contrib import admin
from .models import NewsletterSubscriber


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'goal', 'wants_starter_plan', 'created_at')
    search_fields = ('email', 'goal')
    list_filter = ('goal', 'wants_starter_plan', 'created_at')
