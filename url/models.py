from django.db import models

# Create your models here.


class url_db(models.Model):
    og = models.URLField()
    short = models.CharField(max_length=10, unique=True)
