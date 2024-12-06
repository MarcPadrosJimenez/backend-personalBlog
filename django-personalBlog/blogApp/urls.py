from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('newPost/', views.PostCreateView.as_view()),
    path('posts/', views.post_list, "post_list"),
]