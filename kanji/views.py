import json
import random

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

from .models import Character, FlashCard

# Create your views here.


@login_required(login_url="login/")
def main(request):
    boxs = FlashCard.objects.filter(user=request.user)
    boxs_cont = [boxs.filter(box=n).count() for n in range(1, 6)]
    num = request.GET.get("q", 0)

    context = {"boxs": boxs_cont, "num": num}
    return render(request, "kanji/main.html", context)


def characters_view(request):
    tableSearch = request.GET.get("table_search", "")
    characters = Character.objects.filter(grade__in=tableSearch) if tableSearch.isnumeric() else Character.objects.filter(
        Q(character=tableSearch)
        | Q(meaning__icontains=tableSearch)
        | Q(onyomi__icontains=tableSearch)
        | Q(kunyomi__icontains=tableSearch)
    )

    p = request.GET.get("p")
    paginator = Paginator(characters, per_page=100)
    pages = paginator.get_page(p)

    context = {"pages": pages}
    return render(request, "kanji/characters.html", context)


def character_view(request, letter):
    character = Character.objects.get(character=letter)
    context = {"char": character}
    return render(request, "kanji/character.html", context)
