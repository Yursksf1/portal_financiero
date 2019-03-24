from django.contrib import admin
from .models import Inversion

# Register your models here.

class InversionAdmin(admin.ModelAdmin):
    list_display    = ( 'id', 'descripcion', 'interes', 'monto', 'creacion')
    list_filter     = ('interes', 'monto', 'creacion')
    search_fields   = ('id', 'descripcion','interes', 'monto', 'creacion')





admin.site.register(Inversion, InversionAdmin)