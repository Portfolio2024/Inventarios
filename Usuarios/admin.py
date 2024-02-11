from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'direccion', 'localidad', 'telefono')
    search_fields = ('user', 'direccion', 'localidad', 'telefono')
    list_filter = ('localidad',)


admin.site.register(Profile, ProfileAdmin)



# Register your models here.
