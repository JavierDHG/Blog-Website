from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('post/', views.show_post, name='show_post'),
    path('ViewPost/<int:id>', views.view_post, name='view_post'),
    path('profile/', views.profile, name='profile'),
    path('my_post/', views.my_post, name='my_post'),
    path('add_comment/<int:id>/', views.my_comments, name='add_comment'),
    path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:id>/', views.delete_post, name='delete_post'),
]