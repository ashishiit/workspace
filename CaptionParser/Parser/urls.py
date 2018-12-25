'''
Created on Jul 26, 2018

@author: S528358
'''
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    path('uploads/', views.model_form_upload, name='model_form_upload'),
    path('test_uploads/', views.uploadView, name='uploadView'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)