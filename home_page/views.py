from django.shortcuts import render

# Create your views here.

def MainPage(request):
    # Your view logic goes here
    return render(request,'home.html')

def Shop(request):
    return render(request, 'shop.html')
