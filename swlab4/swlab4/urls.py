from django.contrib import admin
from django.urls import path

from swlab4.swlab4.views import GatewayAPI, ClientRegister, ClientLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/gateway-api', GatewayAPI.as_view({'post': 'list'}), name='gateway-api'),
    path('api/client-register', ClientRegister.as_view({'post': 'list'}), name='client-register'),
    path('api/client-login', ClientLogin.as_view({'post': 'list'}), name='client-login'),
]
