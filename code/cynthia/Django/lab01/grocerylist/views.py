from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from django.http import HttpResponseRedirect
from .models import GroceryItem

#returns list
def index(request):
    latest_list = GroceryItem.objects.order_by('-created_date')
    context = {'latest_list': latest_list,}
    return render(request, 'grocerylist/index.html', context)



def add(request):
    item_description = request.POST['add_item']
    item = GroceryItem(item_description=item_description)
    item.save()
    return HttpResponseRedirect(reverse('grocerylist:index'))
#instead of rendering it redirects to index, only takes post requests


#checks for things done
def done(request,item_id):
    # purchased_item = GroceryItem.get(pk=item_id)
    # if purchased_item == True:
    #     purchased_item.save()
    #purchased item.completed = true, then save
    return HttpResponseRedirect(reverse('grocerylist:index'))



#redirect instead of render new template, will need to add more forms onto main template
#item_id to get groceryitem.pk .id


