from django.db import models


class NewsletterSubscriber(models.Model):
    GOAL_CHOICES = [
        ('weight_loss', 'Weight loss'),
        ('wellness_longevity', 'Wellness and longevity'),
        ('energy_vitality', 'Energy and vitality'),
        ('balance_mobility', 'Balance and mobility'),
    ]

    email = models.EmailField(unique=True)
    goal = models.CharField(max_length=50, choices=GOAL_CHOICES, blank=True)
    wants_starter_plan = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email