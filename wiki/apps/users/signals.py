from django.db.models.signals import post_save, pre_delete, pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from django.core.mail import mail_admins, send_mail
from django.conf import settings


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User, dispatch_uid='register')
def register(sender, instance, **kwargs):
    if kwargs.get('created', False):
        mail_admins('Richiesta iscrizione utente', 
        f"È stata effettuata una richiesta di iscrizione dall'utente:\n\n{ instance.username }\n{ instance.email }\n\nPer effettuare operazioni vai a http://127.0.0.1:8000/admin",
        fail_silently=False, )


@receiver(pre_save, sender=User, dispatch_uid='active')
def active(sender, instance, **kwargs):
    if instance.is_active and User.objects.filter(pk=instance.pk, is_active=False).exists():
        subject = 'Attivazione Account'
        mesagge = '%s il tuo account è stato attivato con successo' %(instance.username)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, mesagge, from_email, [instance.email], fail_silently=False)


@receiver(pre_delete, sender=User, dispatch_uid='delete')
def delete_account(sender, instance, **kwargs):
        subject = 'Account eliminato'
        mesagge = '%s, il tuo account è stato eliminato con successo' %(instance.username)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, mesagge, from_email, [instance.email], fail_silently=False)