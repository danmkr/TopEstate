from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

from Home.forms import SearchForm
from Home.models import Search
from createPost.models import Anunt, Promovare


class HomeTemplateView(CreateView, ListView):
    template_name = 'Home/homepage.html'
    model = Search, Promovare, Anunt
    context_object_name = 'all_announce'
    form_class = SearchForm
    def get_queryset(self):
        return Promovare.objects.filter(tip_anunt='TL')
