from django.urls import path
from generic_app import views1
urlpatterns=[
   path('genericlistcreate/',views1.glistcreate.as_view(),name='listcreate') ,
   path('genericlistcreate/<int:pk>/',views1.glistcreate.as_view(),name='listcreate') ,
   path('studentupdate_d/<int:pk>/',views1.student_u_d.as_view(),name='listcreate') ,
   
   
]