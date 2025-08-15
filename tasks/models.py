from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):

    title = models.CharField(max_length=200)
    description =  models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    def __str__(self):
        return self.title