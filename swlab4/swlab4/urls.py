from django.contrib import admin
from django.urls import path

from swlab4.swlab4.views import GatewayAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/gateway-api', GatewayAPI.as_view({'post': 'list'}), name='gateway-api'),
]
