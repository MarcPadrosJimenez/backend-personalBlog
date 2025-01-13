from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('sections',views.create_section, name="create_section"),
    path('sections/<str:section_name>/posts/create', views.create_post, name="create_post"),
    path('sections/<str:section_name>/posts', views.get_section_posts, name="get_section_posts"),
    path('posts/<int:post_id>/update', views.update_post, name="update_post"),
    path('posts/<int:post_id>/delete', views.delete_post, name="delete_post"),
]