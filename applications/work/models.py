from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion") 
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class Project(models.Model):
    name = models.CharField(max_length = 25, verbose_name="Nombre")
    category = models.ManyToManyField(Category, verbose_name="Categoria")
    description = models.TextField(verbose_name="Descripcion")
    image_project = models.ImageField(upload_to="static/images/portafolio", height_field=None, width_field=None, max_length=100, verbose_name="Imagen")
    customer = models.CharField(max_length = 25, verbose_name="Nombre al que se realizo el proyecto", blank=True)
    url = models.TextField(verbose_name="Url de git")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

class WorkPage(models.Model):
    title = models.CharField(max_length = 150, verbose_name="Titulo")
    project = models.ManyToManyField(Project, verbose_name="Proyecto")
    is_active = models.BooleanField(verbose_name="La pagina esta activa?", default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion") 

    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'