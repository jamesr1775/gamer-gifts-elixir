from django.shortcuts import render

# Create your views here.


def view_shopping_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'shopping_bag/shopping_bag.html')
