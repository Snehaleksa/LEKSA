from django.urls import path
from . import views



urlpatterns = [
    path('',views.index),
    path('create-new-post',views.createPost),
    path('getpost',views.GETAlPosts),
    path('update',views.UpdatePost),
    path('delete',views.DeletePost),
    path('getpostbyid',views.getPost),
]