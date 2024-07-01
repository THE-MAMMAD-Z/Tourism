from django.shortcuts import render ,redirect
from .forms import ContactForm
from .models import Place
from django.contrib import messages
from django.views.generic.list import ListView
from django.db.models import F, Value, CharField
from django.db.models.functions import Concat
from .models import Place


def home(request):
    types = Place.place_type
    city = Place.objects.values('city').distinct()

    return render(request, 'home/index.html',{'city':city.values,"types":types})


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


def places(request,code):
    if request.method == 'POST':
        if code==1:
            city_name = request.POST.get('city')
            location_name = request.POST.get('makan')
            print(city_name,location_name)
            result = Place.objects.filter(city=city_name,location_type=location_name)
            return render(request , 'list.html',{"objects" : result})

    objects = Place.objects.all()
    return render(request , 'list.html',{"objects" : objects})


