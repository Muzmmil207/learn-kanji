import functools

import requests
from django.core.management.base import BaseCommand
from kanji.models import Character, CharacterExamples


class Command(BaseCommand):
    help = "catching data from the api and stored it in the database"

    def handle(self, *args, **options):
        url = "https://kanjialive-api.p.rapidapi.com/api/public/kanji/all"
        headers = {
            "X-RapidAPI-Key": "e0f3c49045msh92aa2798b32d135p1f09dbjsnbb71683b411e",
            "X-RapidAPI-Host": "kanjialive-api.p.rapidapi.com",
        }
        response = requests.get(url, headers=headers).json()

        for data in response:
            if not Character.objects.filter(character=data["kanji"]["character"]).exists():
                character = Character(
                    character=data["kanji"]["character"],
                    grade=data["references"]["grade"],
                    meaning=data["kanji"]["meaning"]["english"],
                    onyomi="{katakana} ({romaji})".format(**(data["kanji"]["onyomi"])),
                    kunyomi="{hiragana} ({romaji})".format(**(data["kanji"]["kunyomi"])),
                    image=data["radical"]["image"],
                    strokes=functools.reduce(
                        lambda x, y: x + "   " + y, data["kanji"]["strokes"]["images"]
                    ),
                    video=data["kanji"]["video"]["mp4"],
                )
                character.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        "%s has been added to the database" % data["kanji"]["character"]
                    )
                )

                examples = data["examples"]
                for example in examples:
                    CharacterExamples.objects.create(
                        character=character,
                        japanese=example["japanese"],
                        meaning=example["meaning"]["english"],
                        audio=example["audio"]["mp3"],
                    )
