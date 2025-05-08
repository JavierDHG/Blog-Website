from django.contrib import admin

# Register your models here.

from .models import Mis_Posts
from .models import Comentarios

admin.site.register(Mis_Posts)
admin.site.register(Comentarios)