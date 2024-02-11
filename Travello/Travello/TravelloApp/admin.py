from django.contrib import admin
from . models import Nspot,Ispot
# Register your models here.
class NspotAdmin(admin.ModelAdmin):
    list_display=["nspot_id","nspot_name","ncategory","nprice","nimage"]
    
admin.site.register(Nspot,NspotAdmin)

class IspotAdmin(admin.ModelAdmin):
    list_display=["ispot_id","ispot_name","icategory","iprice","iimage"]

admin.site.register(Ispot,IspotAdmin)