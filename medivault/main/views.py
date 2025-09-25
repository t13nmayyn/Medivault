from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'main/main.html')


def about(request):
    return render(request,'main/about.html')

def contact(request):
    return render(request,'main/contact.html')
