from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    user=request.user
    hello= 'hello world'
    context={'user':user,'hello':hello}
    return render(request,'main/home.html',context)