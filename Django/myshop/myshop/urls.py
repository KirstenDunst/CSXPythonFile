'''
Author: Cao Shixin
Date: 2023-04-06 09:02:17
LastEditors: Cao Shixin
LastEditTime: 2023-04-06 09:44:38
Description: 
'''
"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin',admin.site.urls),
    path('index/', view=views.index),
    # 路由包含include(减化项目复杂度)，如果url的第一部分被匹配，则其余部分会在子路由中进行匹配
    path('',view=include('app1.urls')),
    path('', view=include('app2.urls'))
]
