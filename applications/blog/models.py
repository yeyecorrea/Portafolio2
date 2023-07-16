from django.db import models
from .managers import BlogManager, CategoryManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    objects = CategoryManager()
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Tags(models.Model):
    name = models.CharField(max_length = 50, verbose_name="Nombre", blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

class Comment(models.Model):
    name = models.CharField(max_length = 150, verbose_name="Nombre", blank=True)
    image_comment = models.ImageField(upload_to="static/images/blog/comment", height_field=None, width_field=None, max_length=100, verbose_name="Imagen", blank=True, default="static/images/blog/comment")
    email = models.EmailField(verbose_name="Correo", blank=True)
    comment = models.TextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'
        
class Post(models.Model):
    title = models.CharField(max_length = 50, verbose_name="Titulo")
    image_blog = models.ImageField(upload_to="static/images/blog", height_field=None, width_field=None, max_length=100, verbose_name="Imagen")
    content = models.TextField(verbose_name="Contenido")
    view = models.IntegerField(verbose_name="Visitas de la publicacion", default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name="Categoria", related_name="Category_Post")
    tags = models.ManyToManyField(Tags, blank=True, verbose_name="Etiquetas")
    comments = models.ManyToManyField(Comment, verbose_name="Comentarios")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    objects = BlogManager()
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

class Blog(models.Model):
    is_active = models.BooleanField(verbose_name="La pagina esta activa?", default=True)
    post = models.ManyToManyField(Post, verbose_name="Publicaciones")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return f"Blog"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'