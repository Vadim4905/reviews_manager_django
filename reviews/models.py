from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.



class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='reviews')
    pub_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title