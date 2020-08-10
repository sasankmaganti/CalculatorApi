from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Calculation(models.Model):
    created_date = models.DateTimeField(primary_key=True, auto_now_add=True, auto_now=False)
    calculation = models.TextField()
