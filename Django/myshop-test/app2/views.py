'''
Author: Cao Shixin
Date: 2023-04-06 09:33:43
LastEditors: Cao Shixin
LastEditTime: 2023-04-14 15:21:12
Description: 
'''
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest

from app2.models import UserBaseInfo

# Create your views here.
def hello(request):
    return  HttpResponse('Hello Django!!!')

def index(request):
    return HttpResponse('app2中的index方法')

def show(request, id):
    return HttpResponse('app2中的show方法,参数为id,值为:'+str(id))

def show_uuid(request, id):
    return HttpResponse('app2中的show_uuid方法,参数为id,值为：'+str(id))

def show_slug(request, q):
    return HttpResponse('app2中的show_slug方法,参数内容为q,值为:'+str(q))

    # 这里的形参名称year要和urls.py中的接受参数一致
def article_list(request, year):
    return HttpResponse('app2中的article_list方法,参数内容为year,值为:'+str(year))

def article_page(request, page,key):
    return HttpResponse('app2中的article_page方法,参数内容有page(任意数字):%s,key(字母数字下划线):%s'%(page,key))

def url_reverse(request):
    # 使用reverse()方法反向解析
    print('在views()函数中使用reversed()方法解析的结果:%s'%(reversed('app2_url_reverse')))
    return render(request,'2/url_reverse.html')

def test_get(request: HttpRequest):
    # 测试get的请求参数信息获取
    # 获取 域名+端口
    print('>>>get_host():'+request.get_host())
    # 全部路径，包含参数(异常属性get_raw_uri)
    # print('get_raw_uri():'+request.get_raw_uri())
    # 获取访问文件路径，不包含参数
    print('path:'+request.path)
    # 获取访问文件路径，包含参数
    print('get_full_path():'+request.get_full_path())
    # 获取请求中http的方式：eg POST/GET
    print('method:'+request.method)
    # 获取get请求的参数
    print('GET:'+str(request.GET))
    # 用户浏览器的user-agent字符串
    print('user-agent:'+request.META.get('HTTP_USER_AGENT'))
    # 客户端ip地址
    print('remote_addr:'+request.META.get('REMOTE_ADDR'))
    # 获取get参数
    print ('获取get参数username字段:'+str(request.GET.get('username')))
    
    return HttpResponse('')

def hello_world(request: HttpRequest, *args, **kwargs):
    request_info = ""
    request_info += "request.scheme={}\n".format(request.scheme)
    request_info += "request.body={}\n".format(request.body)
    request_info += "request.path={}\n".format(request.path)
    request_info += "request.method={}\n".format(request.method)
    request_info += "request.GET={}\n".format(request.GET)
    request_info += "request.FILES={}\n".format(request.FILES)
    request_info += "request.get_host={}\n".format(request.get_host())
    request_info += "request.get_port={}\n".format(request.get_port())
    request_info += "request.get_full_path={}\n".format(request.get_full_path())
    # request_info += "request.get_raw_uri={}\n".format(request.get_raw_uri())
    request_info += "request.build_absolute_uri={}\n".format(request.build_absolute_uri())

    return HttpResponse(request_info, content_type="text/plain")

def test_post(request:HttpRequest):
    print('>>>>>>method:'+request.method)
    print('参数中的username:'+str(request.POST.get('username')))
    return render(request,'2/test_post.html')


def test_response(request):
    response = HttpResponse()
    response.write('hello django')
    response.write('<br>')
    response.write(response.content)
    response.write('<br>')
    response.write(response['Content-type'])
    response.write('<br>')
    response.write(response.status_code)
    response.write('<br>')
    response.write(response.charset)
    response.write('<br>')
    
    return response

def test_render(response):
    return render(response,'2/test_render.html',{'info':'hello django'},content_type='text/html')


def test_redirect_model(request,id):
    user = UserBaseInfo.objects.get(id=id)
    return render(user)
def userinfo(request, id):
    user = UserBaseInfo.objects.get(id=id)
    return HttpResponse("编号:"+str(user.id)+"姓名:"+user.name)