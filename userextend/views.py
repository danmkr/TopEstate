from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from userextend.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

def logout_view(request):
    logout(request)
    return redirect('/')
