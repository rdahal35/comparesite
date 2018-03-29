from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse
from .models import Mobile, Company

def index(request):
	return render(request,'compare/index.html')

def comparepage(request):
	mobile_list= Mobile.objects.all()
	company_list=Company.objects.all()
	print(mobile_list)
	context={
		'mobile_list':mobile_list,
		'company_list':company_list,
	}

	return render(request,'compare/compare.html',context)

def detail(request,):

	# mobile=get_object_or_404(Mobile, pk=mobile_id)
	return render(request,'compare/detail.html')
	