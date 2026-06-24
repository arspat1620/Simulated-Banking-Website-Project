from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CustomUser)
class AdminModel(admin.ModelAdmin):
    list_display = ['id','username','email','PhoneNumber','balance','is_active']
    list_display_links = ['id','username']
    list_editable = ['balance','is_active']
    search_fields = ['username']
    list_filter = ['is_active']
    list_per_page = 20
    ordering = ['id']