"""boke URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
# 自己加
# from ..news import views
from news import views
from django.conf.urls import url, include
# 项目名为zqxt_views  app名为calc
urlpatterns = [
    # path('admin/', admin.site.urls),
    # url(r'^admin/', admin.site.urls),
    #  http://127.0.0.1:8002/add/?a=4&b=5
    url(r'^add/$', views.add, name='add'),  # 注意修改这一行
    #采用/add/3/4 这样的网址的方式
    url(r'^add2/(\d+)/(\d+)/$', views.add2, name='add2'),
    # url(r'^$',views.index, name='home'),
    url(r'^admin', admin.site.urls),
    url(r'^$',views.home1, name='home'),
    url(r'^string', views.strhome, name='strhome'),
    url(r'list', views.listhome, name='listhome'),
]
