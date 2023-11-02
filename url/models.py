from django.db import models

# Create your models here.


class Link(models.Model):
    og = models.URLField()
    short = models.SlugField(max_length=128, unique=True, db_index=True)
    visit_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.short
