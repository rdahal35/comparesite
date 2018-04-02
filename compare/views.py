from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Mobile, Company
from django.db.models.fields.related import ManyToManyField


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

#Only For testing. Should be changed
def compareMobile(request,obj1,obj2):
    obj1= Mobile.objects.filter(pk = obj1)[0].to_dict()
    obj2= Mobile.objects.filter(pk = obj2)[0].to_dict()
    obj = {key:(value,obj2[key]) for (key,value) in obj1.items()}
    context = {
    'mobiles':obj
    }
    print(context)
    return render(request,'compare/comparision.html',context)
