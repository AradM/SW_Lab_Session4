from django.contrib import admin

from swlab4.swlab4.models import Client, Admin, Book

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass