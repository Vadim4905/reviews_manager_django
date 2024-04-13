from django.forms import ModelForm

from . import models

class ReviewFrom(ModelForm):
    
    class Meta:
        model = models.Review
        fields =(
            'title',
            'content',
        )