from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView

from Home.forms import SearchForm
from Home.models import Search
from createPost.models import Anunt


class HomeTemplateView(CreateView):
    template_name = 'Home/homepage.html'
    model = Search
    form_class = SearchForm

class HomePageView(ListView):
    template_name = 'Home/homepage.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_anunt='C0')


