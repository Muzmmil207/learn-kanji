from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q, F
from django.core.paginator import Paginator

from .models import Character, FlashCard

import random
import json
# Create your views here.


@login_required(login_url='login/')
def main(request):
    boxs = FlashCard.objects.filter(user=request.user)
    boxsCont = [boxs.filter(box=n).count() for n in range(1, 6)]
    num = request.GET.get('q', 0)


    context = {'boxs': boxsCont, 'num': num}
    return render(request, 'kanji/main.html', context)


@login_required(login_url='login/')
def cards_data(request, num):
    user = request.user
    characters = list(
        user.characters.filter(card__box=num).only(
            'id', 'character', 'kunyomi', 'onyomi', 'meaning'
        ).values()
    )

    try:
        cards = random.choices(characters, k=9)
    except IndexError:
        cards = characters

    if request.method == 'POST':
        data = json.loads(request.body)
        charId = data['charId']
        result = data['result']
        character = Character.objects.get(id=charId)
        flashCard = FlashCard.objects.get(character=character, user=user)

        flashCard.moving(result)

        if user.card.filter(box=5) == user.card.all():
            user.next_grade()

    return JsonResponse(cards, safe=False)


@login_required(login_url='login/')
def characters_view(request):
    tableSearch = request.GET.get('table_search', '')
    characters = Character.objects.filter(
        Q(character=tableSearch) |
        Q(grade=tableSearch) |
        Q(meaning__icontains=tableSearch) |
        Q(onyomi__icontains=tableSearch) |
        Q(kunyomi__icontains=tableSearch)
    )

    p = request.GET.get('p')
    paginator = Paginator(characters, per_page=100)
    pages = paginator.get_page(p)

    context = {'pages': pages}
    return render(request, 'kanji/characters.html', context)


@login_required(login_url='login/')
def character_view(request, letter):
    character = Character.objects.get(character=letter)
    context = {'char': character}
    return render(request, 'kanji/character.html', context)