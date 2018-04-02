from django.urls import path

from . import views

app_name='compare'
urlpatterns =[
	path('',views.index, name='index'),
	path('detail/<int:mobile_id>',views.detail, name='detail'),
	path('compare/<int:obj1>and<int:obj2>/',views.compareMobile,name='compare')


]
