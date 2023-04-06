'''
Author: Cao Shixin
Date: 2023-04-06 09:05:44
LastEditors: Cao Shixin
LastEditTime: 2023-04-06 09:11:51
Description: 
'''
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'1/index.html')


