
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.loader import render_to_string
from middletier import permissionsCheck
from django.http import HttpResponse
from django.contrib import messages


def menu(request,u_1):
    if not permissionsCheck(request,False,''):
        messages.add_message(request, messages.ERROR, 'Something went wrong man!')
        return HttpResponse('Denied', status=403)
    d = {}
    from page.views import getItem
    from page.models import Item
    qs = Item.objects.all()
    qs = qs.filter(menu=u_1)
    from django.template import RequestContext
    d['menuItems'] = getItem(qs)
    return render(request,"menu.html",d)

def page(request,u_1):
    if not permissionsCheck(request,False,''):
        messages.add_message(request, messages.ERROR, 'Something went wrong man!')
        return HttpResponse('Denied', status=403)
    d = {}
    from page.views import getPage
    from page.models import Page
    qs = Page.objects.all()
    qs = qs.filter(title=u_1)
    from django.template import RequestContext
    d['pageData'] = getPage(qs)
    return render(request,"page.html",d)

def home(request):
    if not permissionsCheck(request,False,''):
        messages.add_message(request, messages.ERROR, 'Something went wrong man!')
        return HttpResponse('Denied', status=403)
    d = {}
    return render(request,"home.html",d)
