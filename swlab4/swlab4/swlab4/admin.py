from django.contrib import admin

from swlab4.swlab4.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
