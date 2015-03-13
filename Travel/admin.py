from django.contrib import admin
from .models import Image,home,visions,record,mztj,link,xiangce,feature,YDt,fea_index1,fea_history,fea_place,m_hotel,m_visitors

class ImageInfoAdmin(admin.ModelAdmin):
	list_display = ("id","img",)

class homeInfoAdmin(admin.ModelAdmin):
	list_display = ("name1","name2","name3")

class visionsInfoAdmin(admin.ModelAdmin):
	list_display = ("name",)

class recordInfoAdmin(admin.ModelAdmin):
	list_display = ("name","category",)

class linkInfoAdmin(admin.ModelAdmin):
	list_display = ("name",)

class mztjInfoAdmin(admin.ModelAdmin):
	list_display = ("name",)

class xiangceInfoAdmin(admin.ModelAdmin):
	list_display = ("name","date",)

class featureInfoAdmin(admin.ModelAdmin):
	list_display = ("name",)

class YDtInfoAdmin(admin.ModelAdmin):
	list_display = ("title",)

class fea_index1InfoAdmin(admin.ModelAdmin):
	list_display = ("name",)

class fea_historyInfoAdmin(admin.ModelAdmin):
	list_display = ("date",)

class fea_placeInfoAdmin(admin.ModelAdmin):
	list_display = ("name",)

class m_hotelInfoAdmin(admin.ModelAdmin):
	list_display = ("name",)

class m_visitorslInfoAdmin(admin.ModelAdmin):
	list_display = ("name",)


	

admin.site.register(Image,ImageInfoAdmin)
admin.site.register(home,homeInfoAdmin)
admin.site.register(visions,visionsInfoAdmin)
admin.site.register(record,recordInfoAdmin)
admin.site.register(mztj,mztjInfoAdmin)
admin.site.register(link,linkInfoAdmin)
admin.site.register(xiangce,xiangceInfoAdmin)
admin.site.register(feature,featureInfoAdmin)
admin.site.register(YDt,YDtInfoAdmin)
admin.site.register(fea_index1,fea_index1InfoAdmin)
admin.site.register(fea_history,fea_historyInfoAdmin)
admin.site.register(fea_place,fea_placeInfoAdmin)
admin.site.register(m_hotel,m_hotelInfoAdmin)
admin.site.register(m_visitors,m_visitorslInfoAdmin)



