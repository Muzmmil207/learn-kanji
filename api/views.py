import random
import time

from kanji.models import Character, FlashCard
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from .serializers import CharacterSerializer


class CharacterAPIView(APIView):
    authentication_class = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, num):
        if num > 5:
            return Response(HTTP_204_NO_CONTENT)

        user = request.user
        characters = user.characters.filter(card__box=num)

        try:
            cards = random.choices(characters, k=9)
        except IndexError:
            cards = characters

        serializer = CharacterSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request, num):
        user = request.user

        data = request.data
        charId = data["charId"]
        result = data["result"]
        character = Character.objects.get(id=charId)
        flashCard = FlashCard.objects.get(character=character, user=user)

        flashCard.moving(result)
        if (
            FlashCard.objects.filter(user=user, box=5).count()
            == FlashCard.objects.filter(user=user).count()
        ):
            user.next_grade()
            time.sleep(10)
        return Response(HTTP_202_ACCEPTED)
