from django.contrib import admin

# Register your models here.
from .models import Blog, Page

admin.site.register(Blog)
admin.site.register(Page)