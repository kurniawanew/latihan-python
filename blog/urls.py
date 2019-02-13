from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post_list'),
    path('input_post/', views.input_post, name='input_post'),
]