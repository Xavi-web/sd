from django.shortcuts import render, get_object_or_404
from .models import Post, Category   # añadimos la clase del model , para poder cargar los datos de la base de datos
from django.contrib.auth.models import User

# Create your views here.
def blog(request):  
    return render(request,"blog/blog.html", { "blogData": Post.objects.all() } )



def category(request,iid) :  # creamos vista para poder filtrar on line segun el parametro en urls.py
    #category= Category.objects.get(id=category_id)  # en lugar de all filtramos con get(id=variable)
    category= Category.objects.get(id=iid)    # En lugar All creamos lista filtrada
   # category= id=category_id ( Category, id=category_id)   # da error 404 en lugar de error django si el filtro sale en blanco
    return render ( request,"blog/category.html", { "category" : category  } )


def author(request,idAutor) :  # creamos vista para poder filtrar on line segun el parametro en urls.py
    #category= Category.objects.get(id=category_id)  # en lugar de all filtramos con get(id=variable)
    au= User.objects.get(id=idAutor)    # En lugar All creamos lista filtrada
   # category= id=category_id ( Category, id=category_id)   # da error 404 en lugar de error django si el filtro sale en blanco
    return render ( request,"blog/author.html", { "datosAuthor" : au  } )