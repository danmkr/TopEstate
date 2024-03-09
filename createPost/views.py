from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from createPost.forms import AnuntForm, PromoForm
from createPost.models import Anunt, Promovare


class CreatePostView(CreateView):
    template_name = 'createPost/create_post.html'
    model = Anunt
    form_class = AnuntForm
    success_url = reverse_lazy('promo-method')

class PromoMethodView(CreateView):
    template_name = 'createPost/promo_method.html'
    model = Promovare
    form_class = PromoForm
    success_url = reverse_lazy('home')

class Comision0View(ListView):
    template_name = 'createPost/comision_0.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_anunt='C0')

class AgentiiImobiliareView(ListView):
    template_name = 'createPost/agentii_imobiliare.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_anunt='AI')

class AnsambluRezidentialView(ListView):
    template_name = 'createPost/ansamblu_rezidential.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_anunt='AR')

def post(request, pk):
    post = Anunt.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})

class PostDeleteView(DeleteView):
    template_name = 'createPost/delete_post.html'
    model = Anunt
    success_url = reverse_lazy('home')



