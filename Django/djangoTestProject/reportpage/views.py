from django.http import HttpResponse
# Create your views here.
from django.shortcuts import redirect, render


def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    passowrd = request.POST.get('password')
    if username == 'caoshixin' and passowrd == '123456':
      return redirect('/index')
    else:
      return render(request, 'day.html', {"error": "用户名或密码错误"})
  return render(request, 'day.html')

def index(request):
    return render(request, 'index.html')