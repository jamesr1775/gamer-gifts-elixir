from django.shortcuts import render
from django.conf import settings

def index(request):
    """ View to return the index page """
    return render(request, 'home/index.html')

def gift_advice(request):
    """ View to return the index page """
    return render(request, 'home/gift_advice.html')
