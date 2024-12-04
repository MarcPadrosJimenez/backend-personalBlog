from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('newPost/', views.create_post, name='create_post'),
]