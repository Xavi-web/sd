from django.urls import path
from .import views 

urlpatterns = [
    path('blog/', views.blog, name='blog'),                 # app con todos los registros
    path('blog/category/<int:iid>/' , views.category ,name='category'),   #app con los registros filtrados por categoria,  ej: /blog/category/3  donde 3 es el category_id
    path('blog/author/<int:idAutor>/' , views.author ,name='authorURL'),
]    