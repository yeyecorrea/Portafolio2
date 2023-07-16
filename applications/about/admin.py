from django.contrib import admin
from .models import About, Skill, Experience, Knowledge
# Register your models here.
admin.site.register(Knowledge)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(About)
