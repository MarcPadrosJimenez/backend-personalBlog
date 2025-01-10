from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('sections/',views.create_section, name="create_section"),
    path('newPost/', views.create_post, name="create_post"),
    path('<str:section_name>/posts/', views.get_section_posts, name="get_section_posts"),
]