from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Memo_hello(request):
    return HttpResponse("Hello, World! I'm Memo App!")
