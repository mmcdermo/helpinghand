from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

def getItem(args):
    if len(args) == 1:
        return render_to_string('page_Item.html',{ 'obj' : args[0] })
    else:
        return render_to_string('page_ItemList.html',{ 'objs' : args })

def getPage(args):
    if len(args) == 1:
        return render_to_string('page_Page.html',{ 'obj' : args[0] })
    else:
        return render_to_string('page_PageList.html',{ 'objs' : args })
