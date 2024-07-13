from django.urls import path,include
from API_app.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('crud',views.userviewsite,basename='crud1')

urlpatterns = [
   path('',include(router.urls)) 
]
