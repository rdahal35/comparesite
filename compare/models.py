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
		return "%s %dMP" %(self.Size, self.Resolution)

class Processor(models.Model):
	CPU= models.CharField(max_length=100)
	GPU=models.CharField(max_length=100)
	RAM=models.IntegerField()

	def __str__(self):
		return "%s %sGB RAM" %(self.CPU, self.RAM)


class Camera(models.Model):
	Lens=models.CharField(max_length=50, default='-')
	Resolution= models.DecimalField(null=True,max_digits=5, decimal_places=2)
	Flash= models.CharField(max_length=10)
	Secondary_camera=models.DecimalField(null=True,max_digits=5, decimal_places=2)

	def __str__(self):
		return "%s Front %s Back" %(self.Secondary_camera,self.Resolution)


class Battery(models.Model):
	Type= models.CharField(max_length=100)
	Capicity=models.IntegerField()


	def __str__(self):
		return "%s %smA·h" %(self.Type,self.Capicity)

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



class Company(models.Model):
	company_name=models.CharField(max_length=50)

	def __str__(self):
		return self.company_name



class Mobile(models.Model):
	model=models.CharField(max_length=100,verbose_name="Model")
	company= models.ForeignKey(Company,verbose_name="Company",on_delete=models.CASCADE)
	cost = MoneyField(verbose_name="Cost",decimal_places=2,default=0,default_currency='USD',max_digits=11,)
	display=models.ForeignKey(Dispaly,verbose_name="Display",on_delete=models.CASCADE ,null=True, editable=True)
	processor=models.ForeignKey(Processor,verbose_name= "Processor",on_delete=models.CASCADE, null=True,editable=True)
	camera=models.ForeignKey(Camera,verbose_name= "Camera",on_delete=models.CASCADE, null=True,editable=True)
	battery=models.ForeignKey(Battery,verbose_name= "Battery",on_delete=models.CASCADE, null=True,editable=True)
	software=models.ForeignKey(Software,verbose_name= "Software",on_delete=models.CASCADE, null=True,editable=True)
	extraFeature=models.ManyToManyField(extraFeatures,verbose_name= "Extra Features",blank=True,editable=True)

	def to_dict(self):
		d = {}
		for field in Mobile._meta.get_fields():
			if field.name == 'extraFeature':
				try:
					d[field.name] = getattr(self,field.name).all()
				except Exception as e:
					print(e)
			else:
				d[field.name] = str(getattr(self,field.name))
		return d


	def __str__(self):
		return str(self.company)+ str(self.model)
