from django.contrib import admin

from .models import Director

# Register your models here.


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('get_full_name',)
