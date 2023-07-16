from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length = 25, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripcion")
    icon = models.CharField(max_length = 150, verbose_name="Clase del icono")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Lista servicios'
        verbose_name_plural = ''

class Service(models.Model):
    title = models.CharField(max_length=25, verbose_name='titulo')
    subtitle = models.CharField(max_length=150, verbose_name='Descripcion')
    services_list = models.ManyToManyField(Services, verbose_name="Lista de servicios")
    is_active = models.BooleanField(verbose_name="La pagina esta activa?", default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion") 
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name =  'Servicio'