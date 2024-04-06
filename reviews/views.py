from django.shortcuts import render
from . import models
# Create your views here.

def index(request):
    reviews = models.Review.objects.all()
    return render(request,'reviews/index.html',context={'reviews':reviews})