from django.contrib import admin
from models import OrdenCompra, Producto, Estudiante, Acudiente, Profesor


class EstudianteAdmin(admin.ModelAdmin):
    fieldsets = (
            ('Informacion Personal',
                {'fields':['nombre', 'edad', 'telefono']}), 
            ('Informacion colegial',
                {'fields':['carne']}))

    search_fields = ['nombre']

    readonly_fields = ['carne']

    list_display = ['nombre', 'edad', 'telefono', 'carne']

    list_filter = ['edad']

    def save_model(self, request, instance, form, change):
        from random import random
        import math
        if not change:
            instance.carne = str(math.floor(random()*10**6))
        
        instance.save()

admin.site.register(OrdenCompra)
admin.site.register(Producto)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Profesor)
admin.site.register(Acudiente)
