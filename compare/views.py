from django.shortcuts import render
from django.template import loader
# Create your views here.

from django.http import HttpResponse
from .models import Mobile, Company

def index(request):
	mobile_list= Mobile.objects.order_by('-mobile_company')[:5]
	company_list=Company.objects.all()
	context={
		'mobile_list':mobile_list,
		'company_list':company_list,
	}
	return render(request,'compare/compare.html',context)

def detail(request,mobile_id):
	mobile=get_object_or_404(Mobile, pk=mobile_id)
	return render(request,'compare/detail.html',{'mobile':mobile})
	