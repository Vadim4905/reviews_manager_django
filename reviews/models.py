from django.db import models

# Create your models here.


class Review(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)