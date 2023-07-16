from django.db import models
from django.db.models import Manager
from django.db.models import Count

class BlogManager(models.Manager):
    # Metodo que ordena por visita
    def get_popular_posts(self, limit=3):
        result = self.order_by('-view')[:limit]
        return result

class CategoryManager(models.Manager):
    # Metodo que lsita la cantidad de post que hay por categoria
    def catidad_por_categoria(self):
        result = self.annotate(
            num_post=Count('Category_Post')
        )
        return result
