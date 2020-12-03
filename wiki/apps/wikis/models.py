from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField


class WikiCategory(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="nome")
    image = models.ImageField(null=True, blank=True, upload_to="category_images/", default="category_images/default.png", verbose_name="immagine")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="autore")
    date = models.DateTimeField(auto_now=True, verbose_name="data")
    slug = AutoSlugField(populate_from=['name'], unique=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorie"

    def __str__(self):
        return self.name

    def save(self , *args , **kwargs):
        if not self.image:
            self.image = 'category_images/default.png'
            super(WikiCategory, self).save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


class WikiPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="titolo")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="autore")
    date = models.DateTimeField(auto_now=True, verbose_name="data")
    content = models.TextField(verbose_name="contenuto")
    category = models.ForeignKey(WikiCategory, on_delete=models.PROTECT, to_field="slug", verbose_name="categoria")
    slug = AutoSlugField(populate_from=['title'])

    class Meta:
        verbose_name = "wiki guida"
        verbose_name_plural = "wiki guide"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wiki-detail', kwargs={'slug': self.slug})
