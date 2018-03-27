
from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField


# Create your models here.

class Dispaly(models.Model):
	Size=models.CharField(max_length=10)
	Resolution= models.IntegerField()
	Panle=models.CharField(max_length=20)
	Surface=models.CharField(max_length=40)

	def __str__(self):
		return "%s %SMP" %(self.Size, self.Resolution)

class Processor(models.Model):
	CPU= models.CharField(max_length=100)
	GPU=models.CharField(max_length=100)
	RAM=models.IntegerField()

	def __str__(self):
		return "%s %sGB RAM" %(self.CPU, self.RAM)


class Camera(models.Model):
	Lens=models.CharField(max_length=50, null=True)
	Resolution= models.CharField(max_length=20)
	Flash= models.CharField(max_length=10)
	Secondary_camera=models.DecimalField(null=True,max_digits=5, decimal_places=2)

	def __str__(self):
		return "%s Front %s Back" %(self.Secondary_camera,self.Resolution)


class Battery(models.Model):
	Type= models.CharField(max_length=100)
	Capicity=models.IntegerField()


	def __str__(self):
		return "%s %s" %(self.Type,self.Capicity)

class Software(models.Model):
	operating_system=models.CharField(max_length=100)
	operating_system_version=models.CharField(max_length=50)
	KeywordType= models.CharField(max_length=50)

	def __str__(self):
		return "%s %s" %(self.operating_system,self.operating_system_version)



class extraFeatures(models.Model):
	feature_name=models.CharField(max_length=100)
	featur_value=models.CharField(max_length=100)

	def __str__(self):
		return self.feature_name


class Mobile(models.Model):
	mobile_model=models.CharField(max_length=100)
	mobile_company= models.CharField(max_length=200)
	mobile_cost = MoneyField(decimal_places=2,default=0,default_currency='USD',max_digits=11,)
	mobile_display=models.ForeignKey(Dispaly,on_delete=models.CASCADE ,null=True)
	mobile_processor=models.ForeignKey(Processor,on_delete=models.CASCADE, null=True)
	moblie_camera=models.ForeignKey(Camera,on_delete=models.CASCADE, null=True)
	mobile_battery=models.ForeignKey(Battery,on_delete=models.CASCADE, null=True)
	mobile_software=models.ForeignKey(Software, on_delete=models.CASCADE, null=True)
	mobile_extraFeature=models.ForeignKey(extraFeatures,on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.mobile_company+' '+self.mobile_model

