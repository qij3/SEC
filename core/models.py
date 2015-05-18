from django.db import models

# Create your models here.

class Team(models.Model):
    title = models.CharField(max_length=300)
    status = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
