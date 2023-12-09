from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from createPost.forms import AnuntForm
from createPost.models import Anunt


class CreatePostView(CreateView):
    template_name = 'createPost/create_post.html'
    model = Anunt
    form_class = AnuntForm
    success_url = reverse_lazy('home')
