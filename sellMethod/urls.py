from django.urls import path

from sellMethod import views

urlpatterns = [
    path('agentii_imobiliare/vanzari/', views.SellAgentiiImobiliareView.as_view(), name='sell-AI'),
    path('agentii_imobiliare/inchirieri/', views.RentAgentiiImobiliareView.as_view(), name='rent-AI'),
    path('comision_0/vanzari/', views.SellComision0View.as_view(), name='sell-C0'),
    path('comision_0/inchirieri/', views.RentComision0View.as_view(), name='rent-C0'),
    path('ansamblu_rezidential/vanzari/', views.SellAnsambluRezidentialView.as_view(), name='sell-AR'),
    path('ansamblu_rezidential/inchirieri/', views.RentAnsambluRezidentialView.as_view(), name='rent-AR'),
]