'''
Author: Cao Shixin
Date: 2023-04-06 09:34:01
LastEditors: Cao Shixin
LastEditTime: 2023-04-06 09:51:17
Description: 
'''
from django.urls import path
from app2 import views

urlpatterns = [
    path('app2/index/',view=views.index),
    # 动态路由配置（路由参数）
    path('app2/show/<int:id>/',view= views.show)
]
