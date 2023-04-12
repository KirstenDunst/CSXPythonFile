'''
Author: Cao Shixin
Date: 2023-04-06 09:34:01
LastEditors: Cao Shixin
LastEditTime: 2023-04-10 11:30:43
Description: 
'''
from django.urls import path, re_path
from app2 import views

urlpatterns = [
    path('app2/index/',view=views.index),
    # 动态路由配置（路由参数）
    path('app2/show/<int:id>/',view= views.show),
    # 参数数据类型，int（匹配0和正整数）、str（任意非空字符串，不包含”/“，默认类型）、slug（匹配任何ASCII字符串、连接线和下划线）、uuid（uuid字符串，必须包含“-”，所有字母必须小写）
    path('app2/article/<uuid:id>/',view=views.show_uuid,name='show_uuid'),
    path('app2/article/<slug:q>/',view=views.show_slug,name='show_slug'),
    
    # 灵活性更高的re_path()
    re_path('app2/list/(?P<year>\d{4})/',view= views.article_list),
    re_path('app2/list/(?P<page>\d+)&key=(?P<key>\w+)',view=views.article_page,name='article_page'),
    
    # 反向解析路由，即使用name字段，（项目中最好后面也是name不变，只调整path的route即可）
    # name规则：应用名+配置项名称
    path('app2/url_reverse/',view=views.url_reverse,name='app2_url_reverse'),
    
    path('app2/test_get/',view=views.test_get,name='test_get'),
    path('app2/hello_world/',view=views.hello_world,name='app2_hello_world'),
    
    path('app2/test_post/',view=views.test_post,name='app2_test_post'),
    path('app2/test_response/',view=views.test_response,name='app2_test_response'),
]
