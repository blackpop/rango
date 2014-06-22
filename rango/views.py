from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return HttpResponse("Yo Babua! kaisan ho? <a href='/rango/about'>Idhar Click karo</a>")

def aboutwa(request):
	return HttpResponse("<marquee>ee hai table </marquee><a href='/rango'>bhag wapis ja</a>")
