from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password_r(request):
    Characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        Characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))


    if request.GET.get('Numbers'):
        Characters.extend(list('1234567890'))


    if request.GET.get('special'):
        Characters.extend(list('!@#$%&*'))

    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(Characters)

    return render(request, 'generator/password_r.html', {'password': thepassword})

def About(request):
    return render(request, 'generator/About.html')
