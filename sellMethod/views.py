from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from createPost.models import Anunt
from createPost.views import Comision0View, AgentiiImobiliareView, AnsambluRezidentialView


class SellAgentiiImobiliareView(ListView):
    template_name = 'sellMethod/sell_AI.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de vanzare', tip_anunt='AI')


class SellComision0View(ListView):
    template_name = 'sellMethod/sell_C0.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de vanzare', tip_anunt='C0')



class RentAgentiiImobiliareView(ListView):
    template_name = 'sellMethod/rent_AI.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de inchiriat', tip_anunt='AI')

class RentComision0View(ListView):
    template_name = 'sellMethod/rent_C0.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de inchiriat', tip_anunt='C0')

# ANSAMBLU REZIDENTIAL:
# INCHIRIERI:
class RentAnsambluRezidentialView(ListView):
    template_name = 'sellMethod/rent_AR.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de inchiriat', tip_anunt='AR')

class RentAnsambluRezidentialApartamenteView(ListView):
    template_name = 'sellMethod/rent_AR_ap.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de inchiriat', tip_anunt='AR', tip_proprietate='apartamente')

class RentAnsambluRezidentialCaseView(ListView):
    template_name = 'sellMethod/rent_AR_case.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de inchiriat', tip_anunt='AR', tip_proprietate='case/vile')

# VANZARI
class SellAnsambluRezidentialView(ListView):
    template_name = 'sellMethod/sell_AR.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de vanzare', tip_anunt='AR')

class SellAnsambluRezidentialApartamenteView(ListView):
    template_name = 'sellMethod/sell_AR_apartamente.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de vanzare', tip_anunt='AR', tip_proprietate='apartamente')

class SellAnsambluRezidentialCaseView(ListView):
    template_name = 'sellMethod/sell_AR_case.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de vanzare', tip_anunt='AR', tip_proprietate='case/vile')

# General

class AnsambluRezidentialApartamenteView(ListView):
    template_name = 'sellMethod/AR_ap.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_anunt='AR', tip_proprietate='apartamente')

class AnsambluRezidentialCaseView(ListView):
    template_name = 'sellMethod/AR_case.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_anunt='AR', tip_proprietate='case/vile')
