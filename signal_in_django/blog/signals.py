from django.db.models.signals import pre_save , post_save
from django.dispatch import receiver
from .models import Post

@receiver(pre_save , sender=Post , )
def before(sender , instance ,**kwargs):
    print(f"Befor save {instance.title}")

@receiver(post_save , sender=Post , )
def before(sender ,created, instance , **kwargs):
    if created:
        print(f"After save {instance.title}")
    else:
        print(f"After update {instance.title}")