from django.db import models
from ckeditor.fields import RichTextField

class Home(models.Model):
    title = models.CharField(max_length = 25, verbose_name="Titulo", default="Hola Soy un", help_text="El valor debe ser maximo de 20 caracteres")
    description = RichTextField(verbose_name="Descripcion", help_text="El valor debe ser maximo de 150 caracteres", blank=True)
    is_active = models.BooleanField(verbose_name="La pagina esta activa?", default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion") 
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Inicio'