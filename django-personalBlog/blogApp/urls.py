from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('newPost/', views.create_post, "create_post"),
    path('posts/', views.post_list, "post_list"),
]