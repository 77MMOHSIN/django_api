"""
URL configuration for generic_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from generic_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentglist/',views.genericlist.as_view(),name='generic'),
    path('studentcreate/',views.studentCreate.as_view(),name='generic'),
    path('studentgeneric/<int:pk>',views.studentretriev.as_view(),name='generic'),
    path('studentgeneric/<int:pk>',views.studentupdate.as_view(),name='generic12'),
    path('studentglist/<int:pk>',views.studentdelete.as_view(),name='generic12'),
    path('',include('generic_app.urls1'))
]
