from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
	return HttpResponse("hey there <a href='/rango/about'>VISIT ABOUT</a>")

def aboutwa(request):
	return HttpResponse("<marquee>some trolling text lol</marquee><a href='/rango'>Get Back To Rango</a>")

def somepage(request) :
	context = RequestContext(request)
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render_to_response('rango/somepage.html', context_dict, context)


