from django.db import models
from django.contrib.auth.models import User


class StarterPlanProgress(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='starter_plan_progress'
    )
    step_number = models.PositiveSmallIntegerField()
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'step_number')
        ordering = ['step_number']

    def __str__(self):
        return f"{self.user.username} - Step {self.step_number}"
