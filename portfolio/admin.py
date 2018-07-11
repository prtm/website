from django.contrib import admin
from .models import Message
# Register your models here.

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message','created','modified')
    list_filter = ('created', 'modified')
    search_fields = ('name','email','message')
    ordering = ('-modified','-created')
