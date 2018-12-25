'''
Created on Mar 3, 2018

@author: S528358
'''
from django.contrib import admin
from django.urls import path
from imageblog import views
urlpatterns = [
#     path('admin/', admin.site.urls),
    path('', views.posts_home, name = 'posts_home'),
    path('create/', views.posts_create, name = 'posts_create'),
    path('update/', views.posts_update, name = 'posts_update'),
    path('delete/', views.posts_delete, name = 'posts_delete'),
    path('detail/', views.posts_detail, name = 'posts_detail'),
]
