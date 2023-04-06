from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader

from .models import GroceryItem

# Create your views here.
def index(request):
    grocery_list = GroceryItem.objects.order_by('create_date')

    template = loader.get_template('grocery_list/index.html')
    context = {
        'grocery_list': grocery_list,
    }
    return HttpResponse(template.render(context, request))

def add(request):
    return HttpResponseRedirect(reverse)

def complete(request, item_id):
    grocery_item = get_object_or_404(GroceryItem, pk=item_id)
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete(request, item_id):
    grocery_item = get_object_or_404(GroceryItem, pk=item_id)
    return HttpResponseRedirect(reverse('grocery_list:index'))