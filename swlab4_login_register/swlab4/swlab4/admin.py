from django.contrib import admin

from swlab4.swlab4.models import Client, Admin


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    pass
