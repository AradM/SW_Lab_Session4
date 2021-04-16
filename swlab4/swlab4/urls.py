from django.contrib import admin
from django.urls import path

from swlab4.swlab4.views import GatewayAPI, ClientRegister, ClientLogin, ClientProfileView, ClientProfileUpdate
from swlab4.swlab4.views import AdminRegister, AdminLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/gateway-api', GatewayAPI.as_view({'post': 'list'}), name='gateway-api'),
    path('api/client-register', ClientRegister.as_view({'post': 'list'}), name='client-register'),
    path('api/client-login', ClientLogin.as_view({'post': 'list'}), name='client-login'),
    path('api/client-profile-view', ClientProfileView.as_view({'post': 'list'}), name='client-profile-view'),
    path('api/client-profile-update', ClientProfileUpdate.as_view({'post': 'list'}), name='client-profile-update'),
    path('api/admin-register', AdminRegister.as_view({'post': 'list'}), name='admin-register'),
    path('api/admin-login', AdminLogin.as_view({'post': 'list'}), name='admin-login'),
]
