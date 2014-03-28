
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template.loader import render_to_string
from middletier import permissionsCheck
from django.http import HttpResponse
from django.contrib import messages


def home(request):
    if not permissionsCheck(request,False,''):
        messages.add_message(request, messages.ERROR, 'Something went wrong man!')
        return HttpResponse('Denied', status=403)
    d = {}
    return render(request,"home.html",d)
