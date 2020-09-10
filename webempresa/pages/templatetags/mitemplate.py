from django import template
from pages.models import Page

  #tebnemos que registrar el nuevo template en la libreria de templates::
register= template.Library()

@register.simple_tag     #decorador
def carga_paginas():   #conseguir la lista de paginas
    paginas= Page.objects.all()
    return paginas

