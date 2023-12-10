from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView

from createPost.forms import AnuntForm
from createPost.models import Anunt


class CreatePostView(CreateView):
    template_name = 'createPost/create_post.html'
    model = Anunt
    form_class = AnuntForm
    success_url = reverse_lazy('home')


class ListeView:
    pass


class Comision0View(ListView):
    template_name = 'createPost/comision_0.html'
    model = Anunt
    context_object_name = 'all_announce'

class AgentiiImobiliareView(ListView):
    template_name = 'createPost/agentii_imobiliare.html'
    model = Anunt
    context_object_name = 'all_announce'

class AnsambluRezidentialView(ListView):
    template_name = 'createPost/ansamblu_rezidential.html'
    model = Anunt
    context_object_name = 'all_announce'

def comision_o_view(request):
    anunturi = Anunt.objects.filter(tip_anunt='C0')
    return render(request, 'createPost/comision_0.html', {'anunturi': anunturi})

def ansamblu_rezidential_view(request):
    anunturi = Anunt.objects.filter(tip_anunt='AR')
    return render(request, 'createPost/ansamblu_rezidential.html', {'anunturi': anunturi})

def agentii_imobiliare_view(request):
    anunturi = Anunt.objects.filter(tip_anunt='AI')
    return render(request, 'createPost/agentii_imobiliare.html', {'anunturi': anunturi})