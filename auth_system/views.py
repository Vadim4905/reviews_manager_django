from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class LoginView(LoginView):
    template_name = "auth_system/login.html"
    
    
class RegisterView(CreateView):
    template_name = "auth_system/register.html"
    form_class = UserCreationForm
    
    def form_valid(self, form: UserCreationForm):
        user = form.save()
        login(self.request, user)
        return redirect("index")
