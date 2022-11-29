from kanji.models import Character, CharacterExamples, FlashCard
from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    """
    Serializer for Character model
    """

    class Meta:
        model = Character
        fields = (
            "id",
            "character",
            "grade",
            "meaning",
            "onyomi",
            "kunyomi",
            "user",
        )
