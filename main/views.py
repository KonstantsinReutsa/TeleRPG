from django.http import HttpResponse
import os


def main(request):
    return HttpResponse('main.html')


def signup(request):
    return HttpResponse('signup.html')


def games(request):
    return HttpResponse('games.html')


def RPGame(request):
    return HttpResponse('RPGame.html')


def contact(request):
    return HttpResponse('contact.html')


def start(request):
    os.system("START /B py Telebot/Telebot.py")
    return HttpResponse('bot started')


def start_game(request):
    os.system("START /B py RPG.py")
    return HttpResponse('game started')


def stop(request):
    return HttpResponse("bot stop")


def answer(request):
    return HttpResponse("")
