from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader
from django.utils import timezone

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
    new_item = request.POST['new-item']
    item_name = new_item
    new_item = GroceryItem()
    new_item.text_description = item_name
    new_item.create_date = timezone.now()
    new_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def complete(request, item_id):
    grocery_item = get_object_or_404(GroceryItem, pk=item_id)
    grocery_item.complete = True
    grocery_item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def remove(request, item_id):
    grocery_item = get_object_or_404(GroceryItem, pk=item_id)
    grocery_item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))