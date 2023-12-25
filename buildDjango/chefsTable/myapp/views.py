from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myapp(request):
    content="<html><h1>Hi Shreyas</h1></html>"
    return HttpResponse(content)