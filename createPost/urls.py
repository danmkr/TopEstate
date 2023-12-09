from django.urls import path

from createPost import views

urlpatterns = [
    path('create_post/', views.CreatePostView.as_view(), name='create-post')
]