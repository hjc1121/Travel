from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Travel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'Travel.views.index'),
    url(r'^index$', 'Travel.views.index'),
    url(r'^visitor$', 'Travel.views.visitors'),	
	url(r'^Photo$', 'Travel.views.Photo'),
    url(r'^testimonials$','Travel.views.Testimonial'),
    	url(r'^Wkfeature$', 'Travel.views.WK_feature'),
	url(r'^fea-indexs$', 'Travel.views.fea_indexs'),
    url(r'^ydtravel$','Travel.views.ydtravel'),
    url(r'^ydtindex$','Travel.views.ydtindex'),
    url(r'^hotel$','Travel.views.hotels'),
    url(r'^register$','Travel.views.registers'),
    url(r'^contact$','Travel.views.contacts'),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
 	{'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)
