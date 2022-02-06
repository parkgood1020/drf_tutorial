from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .quickstart import views

routers = routers.DefaultRouter()
routers.register(r'users', views.UserViewSet)
routers.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('snippets/', include('snippets.urls'))
]
