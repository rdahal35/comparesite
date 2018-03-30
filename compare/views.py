from django.shortcuts import render
from django.template import loader
from django.views.generic import ListView, CreateView, UpdateView

from django.urls import reverse_lazy
# Create your views here.

from django.http import HttpResponse
from .models import Mobile, Company

def index(request):
	return render(request,'compare/index.html')

def comparepage(request):
	company_list=Company.objects.all()
	mobile_list= Mobile.objects.all()
	context={
		'mobile_list':mobile_list,
		'company_list':company_list,
	}

	return render(request,'compare/compare.html',context)


def detail(request,):

	# mobile=get_object_or_404(Mobile, pk=mobile_id)
	return render(request,'compare/detail.html')
