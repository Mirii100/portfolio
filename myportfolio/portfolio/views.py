from django.shortcuts import render
from .models import PortfolioItem,Profile
# Create your views here.

def index(request):
    items=Profile.objects.all()
    return render (request,'index.html',{'items':items})


def base(request):
    items=Profile.objects.all()
    return render (request,'base.html',{'items':items})  

def portfolio(request):
    items = PortfolioItem.objects.all()
    return render(request,'portfolio.html',{'items': items})

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def resume(request):
    return render(request,'resume.html')
def skills(request):
    return render(request,'skills.html')