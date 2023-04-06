'''
Author: Cao Shixin
Date: 2023-04-06 09:34:07
LastEditors: Cao Shixin
LastEditTime: 2023-04-06 09:42:15
Description: 
'''
from django.urls import path
from app1 import views

urlpatterns = [
    path('app1/index',view=views.index)
]
