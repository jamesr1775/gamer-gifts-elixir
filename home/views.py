from django.shortcuts import render


def index(request):
    """ View to return the index page """
    return render(request, 'home/index.html')


def gift_advice(request):
    """ View to return the index page """
    return render(request, 'home/gift_advice.html')


def printing_info(request):
    """ View to return the index page """
    return render(request, 'home/printing_info.html')
