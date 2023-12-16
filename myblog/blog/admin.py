from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Comment)

@admin.register(Post)
class PostAdminView(admin.ModelAdmin):
    list_display = ('user', 'title')
