from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from django.http import HttpResponseRedirect
from .models import GroceryItem

def index(request):
    latest_list = GroceryItem.objects.order_by('-created_date')
    context = {'latest_list': latest_list}
    return render(request, 'grocerylist/index.html', context)


def add(request):
    item_description = request.POST['add_item']
    item = GroceryItem(item_description=item_description)
    item.save()
    return HttpResponseRedirect(reverse('grocerylist:index'))

def done(request,item_id):
    purchased_item = GroceryItem.objects.get(pk=item_id)
    purchased_item.is_completed = True
    purchased_item.save()
    return HttpResponseRedirect(reverse('grocerylist:index'))


def delete(request, item_id):
    delete_item = GroceryItem.objects.get(pk=item_id)

    delete_item.delete()
    return HttpResponseRedirect(reverse('grocerylist:index'))

