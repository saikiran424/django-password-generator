from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request,'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('UpperCase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('SpecialCharacters'):
        characters.extend(list('~!@#$%^&*_-=+'))

    length = int(request.GET.get('length',12))
    thepassword = ''
    for i in range(length):
        thepassword += random.choice(characters) 
    return render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')