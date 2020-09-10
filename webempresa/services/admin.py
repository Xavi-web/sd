from django.contrib import admin
from .models import Service    # añadir el modelo de esta app
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):        # creamos clase para que el modelo pueda tratarse desde admin
    readonly_fields=('created','updated')

admin.site.register (Service, ServiceAdmin)    #registramos el servicio admin

