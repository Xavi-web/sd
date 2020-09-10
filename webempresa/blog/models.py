from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User #modelo de los usuarios del panel admin

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100, help_text="Máximo 100 carácteres", verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True, verbose_name="F. creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="F. modificación")

    class Meta:
        verbose_name="categoría"
        verbose_name_plural="categorías"
        ordering=['-updated']

    def __str__(self):
        return self.name

class Post(models.Model):
    title=  models.CharField(max_length=100,  verbose_name="Título")
    content= models.TextField(verbose_name="Contenido")
    published=models.DateTimeField(verbose_name="Fecha de publicación",default=now )
    image= models.ImageField(verbose_name="Imagen",upload_to="blog",null=True,blank=True)
    author=models.ForeignKey(User ,verbose_name="Autor",on_delete=models.CASCADE  , related_name="autores")  # campo clave externa de relación . On_delete=models.PROTECT  null=True,blank=True
    categories=models.ManyToManyField(Category, verbose_name="Categoría" , related_name="get_posts")      # campo clave externa muchos a muchos hacia otra clase. get_posts
    created=models.DateTimeField(auto_now_add=True, verbose_name="F. creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="F. modificación")    

    class Meta:
        verbose_name="entrada"
        verbose_name_plural="entradas"
        ordering=['-updated']

    def __str__(self):
        return self.title   

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url 
        else:
            return None

    def darCategorias(self):
        return ", ".join( [c.name for c in self.categories.all().order_by("name")] )