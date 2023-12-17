from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from createPost.models import Anunt
from createPost.views import Comision0View, AgentiiImobiliareView, AnsambluRezidentialView

#region 1. Agentii imobiliare

class AgentiiImobiliareApartamenteView(ListView):
    template_name = 'sellMethod/AI_ap.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_anunt='AI', tip_proprietate='apartamente')

class AgentiiImobiliareCaseView(ListView):
    template_name = 'sellMethod/AI_case.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_anunt='AI', tip_proprietate='case/vile')

class AgentiiImobiliareTerenuriView(ListView):
    template_name = 'sellMethod/AI_terenuri.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_anunt='AI', tip_proprietate='terenuri')

#Vanzari
class SellAgentiiImobiliareView(ListView):
    template_name = 'sellMethod/sell_AI.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de vanzare', tip_anunt='AI')

class SellAgentiiImobiliareApartamenteView(ListView):
    template_name = 'sellMethod/sell_AI_ap.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de vanzare', tip_anunt='AI', tip_proprietate='apartamente')

class SellAgentiiImobiliareCaseView(ListView):
    template_name = 'sellMethod/sell_AI_case.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de vanzare', tip_anunt='AI', tip_proprietate='case/vile')

class SellAgentiiImobiliareTerenuriView(ListView):
    template_name = 'sellMethod/sell_AI_terenuri.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de vanzare', tip_anunt='AI', tip_proprietate='terenuri')

# Inchirieri
class RentAgentiiImobiliareView(ListView):
    template_name = 'sellMethod/rent_AI.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de inchiriat', tip_anunt='AI')

class RentAgentiiImobiliareApartamenteView(ListView):
    template_name = 'sellMethod/rent_AI-ap.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de inchiriat', tip_anunt='AI', tip_proprietate='apartamente')

class RentAgentiiImobiliareCaseView(ListView):
    template_name = 'sellMethod/rent_AI_case.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de inchiriat', tip_anunt='AI', tip_proprietate='case/vile')

class RentAgentiiImobiliareTerenuriView(ListView):
    template_name = 'sellMethod/rent_AI_terenuri.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de inchiriat', tip_anunt='AI', tip_proprietate='terenuri')

#endregion

# region 2. Comision 0
class SellComision0View(ListView):
    template_name = 'sellMethod/sell_C0.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de vanzare', tip_anunt='C0')

class RentComision0View(ListView):
    template_name = 'sellMethod/rent_C0.html'
    model = Anunt
    context_object_name = 'all_announce'
    def get_queryset(self):
        return Anunt.objects.filter(tip_vanzare='de inchiriat', tip_anunt='C0')


# endregion

#region 3. ANSAMBLU REZIDENTIAL:
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

#endregion