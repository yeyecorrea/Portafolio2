from django.db import models

# Create your models here.
class Knowledge(models.Model):
    name = models.CharField(max_length = 50, verbose_name="Nombre tus conocimientos")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion") 
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Conocimiento'
        verbose_name_plural = 'Conocimientos'

class Experience(models.Model):
    title = models.CharField(max_length = 50, verbose_name="Titulo", default="Work Experiences")
    name = models.CharField(max_length = 150)
    start_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Fecha de inicio de la experiencia")
    end_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Fecha final de la experiencia")
    description = models.TextField(verbose_name="Descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion") 
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'

class Skill(models.Model):
    title = models.CharField(max_length = 25, verbose_name="Titulo", default="My Skills")
    name = models.CharField(max_length = 25, verbose_name="Nombre de la tecnologia")
    porcentage = models.CharField(max_length = 10, verbose_name="Porcentaje")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion") 

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

class About(models.Model):
    name = models.CharField(max_length = 25, verbose_name="Nombre")
    image_about = models.ImageField(upload_to="static/images/about", height_field=None, width_field=None, max_length=100, verbose_name="Imagen")
    subtitle = models.CharField(max_length = 150, verbose_name="Subtitle")
    description = models.TextField(verbose_name="Descripcion")
    signature = models.ImageField(upload_to="static/images/about", height_field=None, width_field=None, max_length=100, verbose_name="Firma")
    knowledge = models.ManyToManyField(Knowledge, verbose_name="Conocimientos en?")
    experience = models.ManyToManyField(Experience, verbose_name="Experiencia")
    skills = models.ManyToManyField(Skill, verbose_name="Que dominas?")
    is_active = models.BooleanField(verbose_name="La pagina esta activa?", default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Sobre mi'