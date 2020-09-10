from django.contrib import admin
from .models import Category,Post
from django.utils.safestring import mark_safe

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):    # configuramos listado
    list_display=('title','author','published','post_categories','calculado1','imagen')  # campos modo listado
    readonly_fields=('created','updated')   # para modo ficha: campos readonly
    ordering=('author','published')    # modo listado: o por un solo campo: ordering=('author',)
    search_fields=('title','author__username','category__name')        #activar busqueda. Ojo campos relacionados __name
    date_hierarchy='published'
    list_filter=('author__username','categories','published')      # filtros por valor

    def post_categories(self, obj):       #campo calculado, para devolver un campo many to many. obj es el registro
        return ", ".join( [c.name for c in obj.categories.all().order_by("name")] )
    
    post_categories.short_description= "Categorías"   # sobreescribimos el metodo del def creado, para darle un nombre 

    def calculado1(self,obj):
        s= f"<a href='.?aa={obj.author}'>{obj.author}</a>"
        return mark_safe(s)
    calculado1.short_description="Autor"

    def imagen(self, obj):
        if obj.image :
            s=mark_safe(f"<img src='{obj.image.url}' style='width:20%'>")
        else:
            s=''
        return s

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

