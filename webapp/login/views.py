from django.shortcuts import render

# Create your views here.
def Login_Home(request):
    return render(request, 'login.html')
