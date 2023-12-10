from django.urls import path

from sellMethod import views

urlpatterns = [
    path('sell_AI/', views.SellAgentiiImobiliareView.as_view(), name='sell-AI'),
    path('rent_AI/', views.RentAgentiiImobiliareView.as_view(), name='rent-AI'),
    path('sell_C0/', views.SellComision0View.as_view(), name='sell-C0'),
    path('rent_C0/', views.RentComision0View.as_view(), name='rent-C0'),
    path('sell_AR/', views.SellAnsambluRezidentialView.as_view(), name='sell-AR'),
    path('rent_AR/', views.RentAnsambluRezidentialView.as_view(), name='rent-AR'),
]