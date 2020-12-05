# Generated by Django 3.1.3 on 2020-12-05 14:38

import apps.wikis.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='nome')),
                ('image', models.ImageField(blank=True, default='category_images/default.png', null=True, upload_to=apps.wikis.models.category_upload_to, verbose_name='immagine')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='data creazione')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='data ultima modifica')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['name'], unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='autore')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorie',
            },
        ),
        migrations.CreateModel(
            name='WikiPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='titolo')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='data creazione')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='data ultima modifica')),
                ('content', models.TextField(verbose_name='contenuto')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=['title'])),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='autore')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wikis.wikicategory', to_field='slug', verbose_name='categoria')),
            ],
            options={
                'verbose_name': 'wiki guida',
                'verbose_name_plural': 'wiki guide',
            },
        ),
    ]
