from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from Home.forms import SearchForm
from Home.models import Search


class HomeTemplateView(CreateView):
    template_name = 'Home/homepage.html'
    model = Search
    form_class = SearchForm


