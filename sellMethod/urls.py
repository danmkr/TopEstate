from django.urls import path

from sellMethod import views

urlpatterns = [
    path('agentii_imobiliare/vanzari/', views.SellAgentiiImobiliareView.as_view(), name='sell-AI'),
    path('agentii_imobiliare/vanzari/apartamente/', views.SellAgentiiImobiliareApartamenteView.as_view(), name='sell-AI-ap'),
    path('agentii_imobiliare/vanzari/case_vile/', views.SellAgentiiImobiliareCaseView.as_view(), name='sell-AI-case'),
    path('agentii_imobiliare/vanzari/terenuri/', views.SellAgentiiImobiliareTerenuriView.as_view(), name='sell-AI-terenuri'),
    path('agentii_imobiliare/inchirieri/', views.RentAgentiiImobiliareView.as_view(), name='rent-AI'),
    path('agentii_imobiliare/inchirieri/apartamente/', views.RentAgentiiImobiliareApartamenteView.as_view(), name='rent-AI-ap'),
    path('agentii_imobiliare/inchirieri/case_vile/', views.RentAgentiiImobiliareCaseView.as_view(), name='rent-AI-case'),
    path('agentii_imobiliare/inchirieri/terenuri/', views.RentAgentiiImobiliareTerenuriView.as_view(), name='rent-AI-terenuri'),
    path('agentii_imobiliare/apartamente/', views.AgentiiImobiliareApartamenteView.as_view(), name='AI-ap'),
    path('agentii_imobiliare/case_vile/', views.AgentiiImobiliareCaseView.as_view(), name='AI-case'),
    path('agentii_imobiliare/terenuri/', views.AgentiiImobiliareTerenuriView.as_view(), name='AI-terenuri'),
    path('comision_0/vanzari/', views.SellComision0View.as_view(), name='sell-C0'),
    path('comision_0/vanzari/apartamente/', views.SellComision0ApartamenteView.as_view(), name='sell-C0-ap'),
    path('comision_0/vanzari/case_vile/', views.SellComision0CaseView.as_view(), name='sell-C0-case'),
    path('comision_0/vanzari/terenuri/', views.SellComision0TerenuriView.as_view(), name='sell-C0-terenuri'),
    path('comision_0/inchirieri/', views.RentComision0View.as_view(), name='rent-C0'),
    path('comision_0/inchirieri/apartamente/', views.RentComision0ApartamenteView.as_view(), name='rent-C0-ap'),
    path('comision_0/inchirieri/case_vile/', views.RentComision0CaseView.as_view(), name='rent-C0-case'),
    path('comision_0/inchirieri/terenuri/', views.RentComision0TerenuriView.as_view(), name='rent-C0-terenuri'),
    path('comision_0/terenuri/', views.Comision0TerenuriView.as_view(), name='C0-terenuri'),
    path('comision_0/apartamente/', views.Comision0ApartamenteView.as_view(), name='C0-ap'),
    path('comision_0/case_vile/', views.Comision0CaseView.as_view(), name='C0-case'),
    path('ansamblu_rezidential/vanzari/', views.SellAnsambluRezidentialView.as_view(), name='sell-AR'),
    path('ansamblu_rezidential/inchirieri/', views.RentAnsambluRezidentialView.as_view(), name='rent-AR'),
    path('ansamblu_rezidential/vanzari/case_vile/', views.SellAnsambluRezidentialCaseView.as_view(), name='sell-AR-case'),
    path('ansamblu_rezidential/vanzari/apartamente/', views.SellAnsambluRezidentialApartamenteView.as_view(), name='sell-AR-ap'),
    path('ansamblu_rezidential/inchirieri/case_vile/', views.RentAnsambluRezidentialCaseView.as_view(), name='rent-AR-case'),
    path('ansamblu_rezidential/inchirieri/apartamente/', views.RentAnsambluRezidentialApartamenteView.as_view(), name='rent-AR-ap'),
    path('ansamblu_rezidential/case_vile/', views.AnsambluRezidentialCaseView.as_view(), name='AR-case'),
    path('ansamblu_rezidential/apartamente/', views.AnsambluRezidentialApartamenteView.as_view(), name='AR-ap')
]