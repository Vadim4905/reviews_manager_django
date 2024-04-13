from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('create/review',views.create_review,name='review_form'),
]

