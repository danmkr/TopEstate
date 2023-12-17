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
    path('comision_0/inchirieri/', views.RentComision0View.as_view(), name='rent-C0'),
    path('ansamblu_rezidential/vanzari/', views.SellAnsambluRezidentialView.as_view(), name='sell-AR'),
    path('ansamblu_rezidential/inchirieri/', views.RentAnsambluRezidentialView.as_view(), name='rent-AR'),
    path('ansamblu_rezidential/vanzari/case_vile/', views.SellAnsambluRezidentialCaseView.as_view(), name='sell-AR-case'),
    path('ansamblu_rezidential/vanzari/apartamente/', views.SellAnsambluRezidentialApartamenteView.as_view(), name='sell-AR-ap'),
    path('ansamblu_rezidential/inchirieri/case_vile/', views.RentAnsambluRezidentialCaseView.as_view(), name='rent-AR-case'),
    path('ansamblu_rezidential/inchirieri/apartamente/', views.RentAnsambluRezidentialApartamenteView.as_view(), name='rent-AR-ap'),
    path('ansamblu_rezidential/case_vile/', views.AnsambluRezidentialCaseView.as_view(), name='AR-case'),
    path('ansamblu_rezidential/apartamente/', views.AnsambluRezidentialApartamenteView.as_view(), name='AR-ap')
]