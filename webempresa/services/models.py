from django.db import models

# Create your models here.  Despues hay que hacerla accesible desde admin.py
class Service(models.Model):
    title= models.CharField(max_length=200, help_text="Máximo 200 carácteres", verbose_name="Título")
    subtitle= models.CharField(max_length=200, help_text="Máximo 200 carácteres", verbose_name="Subtítulo")    
    content=models.TextField ( verbose_name="Contenido")
    image= models.ImageField( verbose_name="Imagen", upload_to="services")
    created=models.DateTimeField(auto_now_add=True, verbose_name="F. creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="F. modificación")
    

    class Meta:
        verbose_name="servicio"
        verbose_name_plural="servicios"
        ordering=['-updated']

    def __str__(self):
        return self.title