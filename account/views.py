from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect , reverse
from django.urls import reverse_lazy
from django.views import View
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin



class SignUpView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'account/register2.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:home')
        else:
            print("Form errors:", form.errors)  
        return render(request, 'account/register2.html', {'form': form})

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'account/login2.html'
    def get_success_url(self):
            
            return reverse('home:home')



def logout_view(request):
    logout(request)
    return redirect('home:home')



@login_required
def ProfileView(request):
    profile=request.user
    photo=request.user.profile_photo
    context = {
        "profile" : profile,
        "photo" : photo,
    }
    return render(request,'account/profile.html',context)

