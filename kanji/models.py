from accounts.models import User
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

NUM_BOXES = 5
BOXES = range(1, NUM_BOXES + 1)


class Character(models.Model):
    character = models.CharField(max_length=10)
    grade = models.CharField(max_length=7, null=True, blank=True)
    meaning = models.CharField(max_length=100)
    onyomi = models.TextField(null=True, blank=True)
    kunyomi = models.TextField(null=True, blank=True)
    image = models.URLField()
    strokes = models.TextField()
    video = models.URLField()

    user = models.ManyToManyField(User, through="FlashCard", related_name="characters")

    def __str__(self):
        return f"{self.character} grade:  {self.grade}"

    class Meta:
        ordering = ["grade"]


class CharacterExamples(models.Model):
    character = models.ForeignKey(Character, related_name="char", on_delete=models.CASCADE)
    japanese = models.CharField(max_length=1000)
    meaning = models.CharField(max_length=1000)
    audio = models.URLField()

    def __str__(self):
        return f"{self.character}"


class FlashCard(models.Model):

    character = models.ForeignKey(Character, related_name="card", on_delete=models.CASCADE)

    user = models.ForeignKey(User, related_name="card", on_delete=models.CASCADE)

    box = models.IntegerField(choices=zip(BOXES, BOXES), default=BOXES[0])

    def __str__(self):
        return f"User: {self.user.username}  Character: {self.character}"

    def moving(self, bool):
        box = self.box + 1 if bool else BOXES[0]

        if box in BOXES:
            self.box = box
            self.save()
