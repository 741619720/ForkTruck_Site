"""ForkTruck_Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from mysite import views

from django.views.static import serve
from ForkTruck_Site.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Login),
    path('login/article-list.html', views.Task),
    path('login/article-add.html', views.AddTask),
    path('login/test', views.Test),
    url(r'^img/$', views.img, name='img'),
    url(r'^download/(?P<filename>.+)$', views.download, name='download'),
    url(r'^login/download/(?P<filename>.+)$', views.download, name='download'),
]
