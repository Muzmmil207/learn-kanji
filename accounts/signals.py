from django.db.models.signals import post_save
from django.dispatch import receiver
from kanji.models import *

from .models import User


@receiver(post_save, sender=User)
def user_character_level(sender, instance, **kwargs):

    characters = Character.objects.filter(grade=instance.grade)
    for character in characters:
        if not FlashCard.objects.filter(user=instance, character=character).exists():
            FlashCard.objects.create(user=instance, character=character)


# post_save.connect(receiver=user_character_level, sender=User)
