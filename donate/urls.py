"""donate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drop123', drop123),
    path('inssubcribers', inssubcribers),
    path('getsurname', getsurname),
    path('getareaname', getareaname),
    path('drop12', drop12),
    path('login', login),
    path('getreport', getreport),
    path('getarea', getarea),
    path('getcity', getcity),
    path('getstate', getstate),
    path('gsupplierins', gsupplierins),
    path('gcustomerins', gcustomerins),
    path('gproductins', gproductins),
    path('ggetcustomer', ggetcustomer),
    # path('FileUploadView', FileUploadView),
    path('getseclist/', getseclist),
]
