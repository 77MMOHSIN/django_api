from django.contrib import admin
from django.urls import path,include
from API_app import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.show,name="show"),
    path('delete/<int:id>/',views.delete_data, name='deleted'),
    path('<int:id>/',views.update_date, name='updatedata'),
    path('update/',views.thank, name='thank'),
    path('api/',include('API_app.api.urls'))
    
]
