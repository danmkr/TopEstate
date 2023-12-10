from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from createPost.forms import AnuntForm
from createPost.models import Anunt


class CreatePostView(CreateView):
    template_name = 'createPost/create_post.html'
    model = Anunt
    form_class = AnuntForm
    success_url = reverse_lazy('home')

class Comision0View(TemplateView):
    template_name = 'createPost/comision_0.html'

class AgentiiImobiliareView(TemplateView):
    template_name = 'createPost/agentii_imobiliare.html'

class AnsambluRezidentialView(TemplateView):
    template_name = 'createPost/ansamblu_rezidential.html'

def comision_o_view(request):
    anunturi = Anunt.objects.filter(tip_anunt='C0')
    return render(request, 'createPost/comision_0.html', {'anunturi': anunturi})

def ansamblu_rezidential_view(request):
    anunturi = Anunt.objects.filter(tip_anunt='AR')
    return render(request, 'createPost/ansamblu_rezidential.html', {'anunturi': anunturi})

def agentii_imobiliare_view(request):
    anunturi = Anunt.objects.filter(tip_anunt='AI')
    return render(request, 'createPost/agentii_imobiliare.html', {'anunturi': anunturi})