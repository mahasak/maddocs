from django.shortcuts import render
from django.http import HttpResponse
from core.classes import UserManagement
from django.template import RequestContext, loader
# Create your views here.


def index(request):
    a = UserManagement()
    return render(request, 'core/index.html')
    #template = loader.get_template('index.html')
    #context = RequestContext(request)
    #return HttpResponse(template.render(context))

    #return HttpResponse("<html><head></head><body>Hello, world. You're at the polls index." +  a.get_hello()+ request.META['REMOTE_ADDR'] + "</body></html>")