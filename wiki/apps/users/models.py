from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField


def profile_upload_to(instance, filename):
    return "profile_images/{}/{}".format(instance.slug, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from=['user'], unique=True)
    image = models.ImageField(null=True, blank=True, upload_to=profile_upload_to, default="profile_images/default.png")

    def __str__(self):
        return self.user.username

    def save(self , *args , **kwargs):
        if not self.image:
            self.image = 'profile_images/default.png'
            super(Profile, self).save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = "profilo"
        verbose_name_plural = "profili"
