# Generated by Django 4.2.3 on 2023-07-16 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Work Experiences', max_length=50, verbose_name='Titulo')),
                ('name', models.CharField(max_length=150)),
                ('start_date', models.DateField(verbose_name='Fecha de inicio de la experiencia')),
                ('end_date', models.DateField(verbose_name='Fecha final de la experiencia')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Experiencia',
                'verbose_name_plural': 'Experiencias',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre tus conocimientos')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Conocimiento',
                'verbose_name_plural': 'Conocimientos',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='My Skills', max_length=25, verbose_name='Titulo')),
                ('name', models.CharField(max_length=25, verbose_name='Nombre de la tecnologia')),
                ('porcentage', models.CharField(max_length=10, verbose_name='Porcentaje')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Nombre')),
                ('image_about', models.ImageField(upload_to='static/images/about', verbose_name='Imagen')),
                ('subtitle', models.CharField(max_length=150, verbose_name='Subtitle')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('signature', models.ImageField(upload_to='static/images/about', verbose_name='Firma')),
                ('is_active', models.BooleanField(default=True, verbose_name='La pagina esta activa?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
                ('experience', models.ManyToManyField(to='about.experience', verbose_name='Experiencia')),
                ('knowledge', models.ManyToManyField(to='about.knowledge', verbose_name='Conocimientos en?')),
                ('skills', models.ManyToManyField(to='about.skill', verbose_name='Que dominas?')),
            ],
            options={
                'verbose_name': 'Sobre mi',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
