"""
URL configuration for viewset_project project.

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
from viewset_app import views,views1
from rest_framework .routers import DefaultRouter

# creating Router object
router=DefaultRouter()
router1=DefaultRouter()
# register studentviewset with router

# viewset

# router.register('studentapi',views.STudentviewset,basename='student')

#model view set 

router.register('studentapi1',views1.studentmodelview,basename='student')

# readonlyview

router1.register('studentapi',views1.studentreadyonly,basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),


    
    
]
