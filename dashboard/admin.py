from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

admin.site.register(Personal)
admin.site.register(Pedido)
admin.site.site_header = "Sistema de control de Inventarios - Trujillo"
#admin.site.unregister(Group)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','cantidad')
    list_filter = ['categoria']

admin.site.register(Producto, ProductoAdmin)
