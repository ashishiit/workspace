'''
Created on Dec 24, 2018

@author: S528358
'''
from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('', views.sms_response, name='sms'),
]