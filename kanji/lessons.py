from .models import Character, FlashCard, User


import random


class lesson:

    def __init__(self, request):
        self.user = request.user

    def get_characters(self):
        chars = Character.objects.all()
        userChars = FlashCard.objects.filter(user=self.user)
        charArray = [userChars.filter(tracking=n) for n in range(1, 5)]

        index = self.get_index(charArray)
        if index == 1:
            self.create_user_chars()

        data = userChars.select_related('character').filter(tracking=index)[:6]

        return data

    def get_index(self, array):
        for group in array:
            if len(group) == 0:
                return array.index(group)

        return 4

    def create_user_chars(self):
        for item in Character.objects.filter(grade=self.user.level):
            count = 0

            if count == 5:
                break

            try:
                FlashCard.objects.create(user=self.user, character=item)
                count += 1
            except:
                continue
