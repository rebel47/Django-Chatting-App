import re
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.shortcuts import render
import random


def captch(request):
    num=random.randrange(1121,9899)
    global str_num
    str_num=str(num)
    print(str_num)
    return render(request,"register.html",{"img":str_num})

def submit(request):
    if request.method == "POST":
        cap=request.POST.get("captha")
        if str(cap)==str_num :
            return HttpResponse("<h4>YOUR FORM HAS BENN SUBMITED SUCCESSFULLY</h4>")
        else:
            return HttpResponse("<h4>Error captha</h4>")
    else:
        return HttpResponse("<h4>SERVER ERROR</h4>")

def login(request):
    return render(request, 'login.html')

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url =  reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'editProfile.html'
    success_url =  reverse_lazy('home')

    def get_object(self):
        return self.request.user

def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'home.html')