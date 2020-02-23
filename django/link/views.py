from django.shortcuts import render

# Create your views here.

def login(request):
    """トップ画面"""
    return render(request, 'login.html')
