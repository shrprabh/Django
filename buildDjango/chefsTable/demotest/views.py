from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demotest(request):
    path=request.path
    method=request.method
    user=request.user 
    content='''<center><h1>Hello this is a document</h2>
    <p>Request Path {} <p>
    <p>Request Method {}</p>
    <p>Request User {} </p></center>'''.format(path,method,user)
    return HttpResponse(content)
