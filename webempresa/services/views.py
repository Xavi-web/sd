from django.shortcuts import render
from .models import Service   # añadimos el models , para poder cargar los datos de la base de datos

# Create your views here.
def services(request):  
    ss=Service.objects.all()   # cargamos los registros, para usarlos despues en el render
    return render(request,"services/services.html",{'servicesData':ss} )     # pasamos los datos con un parametro web