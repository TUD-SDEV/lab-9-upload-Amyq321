from django.contrib import admin
from .models import book
# Register your models here.

class bookadmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "date_publication")

admin.site.register(book, bookadmin)