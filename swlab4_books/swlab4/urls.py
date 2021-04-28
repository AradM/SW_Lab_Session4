from django.contrib import admin
from django.urls import path

from swlab4.swlab4.views import ClientSeeBooks, CURDGateway, CreateBook, UpdateBook, ReadBook, DeleteBook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/client-see-books', ClientSeeBooks.as_view({'post': 'list'}), name='client-see-books'),
    path('api/curd-gateway', CURDGateway.as_view({'post': 'list'}), name='curd-gateway'),
    path('api/create-book', CreateBook.as_view({'post': 'list'}), name='create-book'),
    path('api/update-book', UpdateBook.as_view({'post': 'list'}), name='update-book'),
    path('api/read-book', ReadBook.as_view({'post': 'list'}), name='read-book'),
    path('api/delete-book', DeleteBook.as_view({'post': 'list'}), name='delete-book'),
]
