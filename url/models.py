from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    og = models.URLField()
    short = models.SlugField(max_length=128, unique=True, db_index=True)
    visit_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.short}"
