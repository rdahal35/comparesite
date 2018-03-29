from django.urls import path

from . import views


urlpatterns =[
	path('',views.index, name='index'),
	path('comparepage/',views.comparepage, name='comparepage'),
	path('<int:pk>/',views.detail, name='detail'),


]
