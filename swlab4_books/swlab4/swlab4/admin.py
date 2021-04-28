from django.contrib import admin

from swlab4.swlab4.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
