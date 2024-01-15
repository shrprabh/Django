from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def allMethods(request):
    path=request.path
    method=request.method
    scheme=request.scheme
    address=request.META['REMOTE_ADDR']
    useragent=request.META['HTTP_USER_AGENT']
    pathinfo=request.path_info
    #updating header
    response=HttpResponse()
    response.headers['age']=20

    msg=f'''
<br/>
<br>Path: {path}
<br>Method:{method}
<br>scheme:{scheme}
<br>address:{address}
<br>user agent:  {useragent}
<br>pathinfo:{pathinfo}
<br>response headers:{response.headers}
'''
    return HttpResponse(msg,content_type='text/html',charset='utf-8')

