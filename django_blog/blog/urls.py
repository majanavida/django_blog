from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<int:post_id>', views.post_comment, name='post_comment'),
]
