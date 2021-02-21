from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,'home.html',{'name':'Home Page'})	


def register(request):
	return render(request,'register.html',{'name':'Register Page'})


def login(request):
	return render(request,'login.html',{'name':'Login Page'})

