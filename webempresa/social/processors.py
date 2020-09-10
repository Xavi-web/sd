from .models import Link

def extender_contexto(request):  #procesadores de contexto, añadir en settings.py  'context_processors': 
    ctx= {}
    links= Link.objects.all()
    for l in links:
        ctx[l.key]=l.url

    return ctx