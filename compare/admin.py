from django.contrib import admin
from .models import Mobile,Dispaly,Processor,Camera,Battery,Software,extraFeatures,Company

# Register your models here.
class MobileAdmin(admin.ModelAdmin):
	pass

admin.site.register(Mobile, MobileAdmin)
admin.site.register(Dispaly)
admin.site.register(Processor)
admin.site.register(Camera)
admin.site.register(Battery)
admin.site.register(Software)
admin.site.register(extraFeatures)
admin.site.register(Company)