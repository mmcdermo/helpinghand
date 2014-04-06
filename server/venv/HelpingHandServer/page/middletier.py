from models import *
from django.core import serializers


#interactions for model Item
from django.http import HttpResponse
def createItem(request):
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken'] #remove this since it is not a part of the object
        from page.forms import ItemForm
        form = ItemForm(data)
        if form.is_valid():
            data = form.cleaned_data
            newItem = form.save()
            newItem.save()
            return HttpResponse('\'Succesfully Created\'')
        return HttpResponse('\'Data Unclean\'')

def retrieveItem(request):
    if request.method == 'POST':
        data = request.POST
        filters = data['filters']
        qs = Item.objects.filter(**filters)
        return HttpResponse(serializers.serialize([qs]))
    return HttpResponse('Please send data as POST')

def deleteItem(request):
    if request.method == 'POST':
        data = request.POST
        filters = data['filters']
        qs = Item.objects.filter(**filters)
        count = 0
        for obj in qs:
            obj.delete()
            count += 1
        return HttpResponse('Deleted %s objects' % count)
    return HttpResponse('Please send data as POST')



#interactions for model Page
from django.http import HttpResponse
def createPage(request):
    if request.method == 'POST':
        data = request.POST.copy()
        del data['csrfmiddlewaretoken'] #remove this since it is not a part of the object
        from page.forms import PageForm
        form = PageForm(data)
        if form.is_valid():
            data = form.cleaned_data
            newPage = form.save()
            newPage.save()
            return HttpResponse('\'Succesfully Created\'')
        return HttpResponse('\'Data Unclean\'')

def retrievePage(request):
    if request.method == 'POST':
        data = request.POST
        filters = data['filters']
        qs = Page.objects.filter(**filters)
        return HttpResponse(serializers.serialize([qs]))
    return HttpResponse('Please send data as POST')

def deletePage(request):
    if request.method == 'POST':
        data = request.POST
        filters = data['filters']
        qs = Page.objects.filter(**filters)
        count = 0
        for obj in qs:
            obj.delete()
            count += 1
        return HttpResponse('Deleted %s objects' % count)
    return HttpResponse('Please send data as POST')

