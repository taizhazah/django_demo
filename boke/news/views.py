from django.shortcuts import render

# Create your views here.
# 首先写一个视图函数
from django.http import HttpResponse

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))

def index(request):
    return render(request,'home.html')

#...此处省略一些代码

def home1(request):
    return render(request, 'home1.html')


def strhome(request):
    string = u'我在自强学堂学习Django,用来建网站'
    return render(request, 'strhome.html', {'string':string})

def listhome(request):
    aaa = ['a','b','c','d','e']
    return render(request, 'listhome.html', {'aaa' : aaa})

def dicthome(request):
    dict = {'site': u'孙小兜', 'content': u'各种IT技术教程'}
    return render(request, 'dicthome.html', {'dict' : dict})
