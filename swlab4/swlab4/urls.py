from django.contrib import admin
from django.urls import path

from swlab4.swlab4.views import GatewayAPI, ClientRegister, ClientLogin, ClientProfileView, ClientProfileUpdate, \
    ClientSeeBooks, CURDGateway, CreateBook, UpdateBook, ReadBook, DeleteBook, AdminSeeClients
from swlab4.swlab4.views import AdminRegister, AdminLogin, AdminProfileView, AdminProfileUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/gateway-api', GatewayAPI.as_view({'post': 'list'}), name='gateway-api'),
    path('api/client-register', ClientRegister.as_view({'post': 'list'}), name='client-register'),
    path('api/client-login', ClientLogin.as_view({'post': 'list'}), name='client-login'),
    path('api/client-profile-view', ClientProfileView.as_view({'post': 'list'}), name='client-profile-view'),
    path('api/client-profile-update', ClientProfileUpdate.as_view({'post': 'list'}), name='client-profile-update'),
    path('api/admin-register', AdminRegister.as_view({'post': 'list'}), name='admin-register'),
    path('api/admin-login', AdminLogin.as_view({'post': 'list'}), name='admin-login'),
    path('api/admin-profile-view', AdminProfileView.as_view({'post': 'list'}), name='admin-profile-view'),
    path('api/admin-profile-update', AdminProfileUpdate.as_view({'post': 'list'}), name='admin-profile-update'),
    path('api/client-see-books', ClientSeeBooks.as_view({'post': 'list'}), name='client-see-books'),
    path('api/curd-gateway', CURDGateway.as_view({'post': 'list'}), name='curd-gateway'),
    path('api/create-book', CreateBook.as_view({'post': 'list'}), name='create-book'),
    path('api/update-book', UpdateBook.as_view({'post': 'list'}), name='update-book'),
    path('api/read-book', ReadBook.as_view({'post': 'list'}), name='read-book'),
    path('api/delete-book', DeleteBook.as_view({'post': 'list'}), name='delete-book'),
    path('api/admin-see-clients', AdminSeeClients.as_view({'post': 'list'}), name='admin-see-clients'),
]
