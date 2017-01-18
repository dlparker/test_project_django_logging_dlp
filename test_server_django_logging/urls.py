"""test_server_django_logging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import targets.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', targets.views.home),
    url(r'^counter/$', targets.views.get_counter),
    url(r'^counter/ajax/$', targets.views.get_counter_ajax),
    url(r'^counter/incr/ajax/$', targets.views.incr_counter_ajax),
]
