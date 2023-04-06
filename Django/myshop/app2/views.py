from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('app2中的index方法')

def show(request, id):
    return HttpResponse('app2中的show方法,参数为id,值为:'+str(id))