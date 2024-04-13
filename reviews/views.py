from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from . import models
from . import forms
# Create your views here.

def index(request):
    reviews = models.Review.objects.all()
    return render(request,'reviews/index.html',context={'reviews':reviews})

@login_required
def create_review(request):
    if request.method == 'GET':
        form =forms.ReviewFrom()
        return render(request,'reviews/review_form.html',context={'form':form})
    elif request.method == 'POST':
        form = forms.ReviewFrom(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('index')