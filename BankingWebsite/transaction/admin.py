from django.contrib import admin
from .models import *

@admin.register(Transaction_History)
class AdminModel(admin.ModelAdmin):
    list_display = ['id','sender','receiver','amount']
    list_display_links = ['id']
    search_fields = ['sender','receiver']
    list_per_page = 20
    ordering=['id']