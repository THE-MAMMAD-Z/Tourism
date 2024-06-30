from django.shortcuts import render ,redirect
from .forms import ContactForm
from .models import Place
from django.contrib import messages


def home(request):
    return render(request, 'home/index.html')


def contact(request):
    
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Message receivd. Thank you!')
            return redirect('home:contact')
    form=ContactForm()     
    return render(request, 'home/contact.html',{'form':form})



def about(request):
    return render(request, 'home/about.html')


def detail(request,num):
    object = Place.objects.get(pk=num)
    return render(request , 'detail.html',{'object':object})


def list(request):
    objects = Place.objects.all()
    return render(request , 'list.html' , {'objects' : objects})