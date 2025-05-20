from django.contrib import admin

# Register your models here.
from .models import Blog, Page, Mis_Posts, Comentarios

admin.site.register(Blog)
admin.site.register(Page)
admin.site.register(Mis_Posts)
admin.site.register(Comentarios)