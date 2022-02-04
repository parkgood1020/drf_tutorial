from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .quickstart import views

routers = routers.DefaultRouter()
routers.register(r'users', views.UserViewSet)
routers.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
