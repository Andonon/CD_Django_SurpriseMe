# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import shuffle
from itertools import islice
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'game/index.html')

def guess(request):
    VALUES = ['All computers wait at the same speed', \
    'A computer program does what you tell it to do, not what you want it to do.', \
    'Intel Inside is a Government Warning required by Law.', \
    'Common sense gets a lot of credit that belongs to cold feet.', \
    'C is quirky, flawed, and an enormous success.', \
    'Chuck Norris counted to infinity, twice!', \
    'ASCII stupid question, get a stupid ANSI!', \
    'A good programmer looks both ways before crossing a one-way street.', \
    'Always code as if the guy who ends up maintaining your code will be a violent psycopath who knows where you live.', \
    'Beta is Latin for still does not work.']
    if request.method == "POST":
        shuffle(VALUES)
        lines = int(request.POST['numoflines'])
        counter = 0
        messages = []
        for element in islice(VALUES, 0, lines):
            messages.append(element)
            counter += 1
        context = {
            "messages": messages
        }
    return render(request, 'game/guess.html', context)
