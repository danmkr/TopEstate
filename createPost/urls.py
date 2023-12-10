from django.urls import path

from createPost import views

urlpatterns = [
    path('create_post/', views.CreatePostView.as_view(), name='create-post'),
    path('comision_0/', views.Comision0View.as_view(), name='comision-0'),
    path('ansamblu_rezidential/', views.AnsambluRezidentialView.as_view(), name='ansamblu-rezidential'),
    path('agentii_imobiliare/', views.AgentiiImobiliareView.as_view(), name='agentii-imobiliare')
]