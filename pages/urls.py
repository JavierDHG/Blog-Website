from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('post/', views.show_post, name='show_post'),
    path('ViewPost/<int:id>', views.view_post, name='view_post'),
]