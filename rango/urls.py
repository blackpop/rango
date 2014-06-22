from django.conf.urls import patterns, url
from django import views

urlpatterns=patterns('',
	url(r'^$',"rango.views.index",name='index'),
	url(r'^about',"rango.views.aboutwa",name='aboutwa'),
	url(r'^loadpage',"rango.views.somepage",name='A page')
)