from django.contrib import admin
from django.utils.html import format_html
from gestion.models import *

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']

class PromocionAdmin(admin.ModelAdmin):
    list_display = ['mostrar_imagen']

    def mostrar_imagen(self, obj):
        if obj.ruta:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.ruta.url))
        return 'No hay imagen'

    mostrar_imagen.short_description = 'Imagen'
    
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['mostrar_imagen']

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="100" height="100" />'.format(obj.imagen.url))
        return 'No hay imagen'

    mostrar_imagen.short_description = 'Imagen'

class PlatilloAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion','mostrar_imagen','visibilidad']
    search_fields = ['nombre']


    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('''
                               <img src="{}" width="100" height="100" />
                               '''.format(obj.imagen.url))
        return 'No hay imagen'

    mostrar_imagen.short_description = 'Imagen'

admin.site.register(Promocion, PromocionAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Mesa)
admin.site.register(Cliente)
admin.site.register(Reservacion)
admin.site.register(Platillo, PlatilloAdmin)

