from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

from Home.forms import SearchForm
from Home.models import Search
from createPost.models import Anunt, Promovare


class HomeTemplateView(CreateView, ListView):
    template_name = 'Home/homepage.html'
    model = Anunt, Promovare
    context_object_name = 'all_announce'
    form_class = SearchForm
    def get_queryset(self):
        return Promovare.objects.filter(metoda_de_promovare='TL')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['searches'] = Search.objects.all()
        context['promovares'] = Promovare.objects.all()
        context['4_tl'] = Anunt.objects.filter(promovare__metoda_de_promovare='TL').order_by('-pret')[:4]
        return context
