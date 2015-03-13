#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from django.template import RequestContext
from Travel.models import home,Image,record,mztj,link,visions,xiangce,feature,YDt,fea_index1,fea_history,fea_place,m_hotel,m_visitors
from django.template.response import TemplateResponse as TR


#主页------------------------------------------------------------------------------------------------------------------------------------


def index(request):
	a1 = home.objects.all()
	visitor =  visions.objects.all()
	Places = record.objects.filter(category="Places")[0:4]
	Climate = record.objects.filter(category="Climate")[0:4]
	Testimonials = record.objects.filter(category="Testimonials")[0:4]
	mzt = mztj.objects.all()[0:3]
	links = link.objects.all()[0:4]
	features = feature.objects.all()[0:6]
	d = {'a1':a1,"Places":Places,"Climate":Climate,"Testimonials":Testimonials,"mzt":mzt,"links":links,"visitor":visitor,"features":features}
	return TR(request,"index.html",d)

#游客相册----------------------------------------------------------------------------------------------------------------------------------


def Photo(request):
	picture = xiangce.objects.all()
	mzt = mztj.objects.all()[0:3]
	links = link.objects.all()[0:4]
	d={"picture":picture,"mzt":mzt,"links":links}
	return TR(request,"photos.html",d)

#游客推荐------------------------------------------------------------------------------------------------------------------------------------

def Testimonial(request):
	mzt = mztj.objects.all()[0:3]
	links = link.objects.all()[0:4]
	d={"mzt":mzt,"links":links}
	return TR(request,"Testimonials.html",d)

#热门景观------------------------------------------------------------------------------------------------------------------------------------

def visitors(request):
	visitor = m_visitors.objects.all()[0:3]
	visitors = m_visitors.objects.all()[3:9]
	mzt = mztj.objects.all()[0:3]
	links = link.objects.all()[0:4]
	d={"visitors":visitors,"visitor":visitor,"mzt":mzt,"links":links}
	return TR(request,"visitor.html",d)


#特色景观------------------------------------------------------------------------------------------------------------------------------------


def WK_feature(request):
	nei = YDt.objects.all()
	mzt = mztj.objects.all()[0:3]
	links = link.objects.all()[0:4]
	d = {"mzt":mzt,"links":links,"nei":nei}
	return TR(request,"WK-feature.html",d)

#知名景观子链接----------------------------------------------------------------------------------------------------------------------------


def fea_indexs(request):
	index1 = fea_index1.objects.all()[0:3]
	history = fea_history.objects.all()[0:3]
	places = fea_place.objects.all()[0:1]
	mzt = mztj.objects.all()[0:3]
	links = link.objects.all()[0:4]
	d = {"index1":index1,"history":history,"places":places,"mzt":mzt,"links":links}
	return TR(request,"fea-index.html",d)

#旅游预订-----------------------------------------------------------------------------------------------------------------------------------


def ydtravel(request):

	return TR(request,"Yd-travel.html")	

def ydtindex(request):
	mzt = mztj.objects.all()[0:3]
	links = link.objects.all()[0:4]
	d = {"mzt":mzt,"links":links}
	return TR(request,"YD-Tindex.html",d)

#酒店预订------------------------------------------------------------------------------------------------------------------------------------

def hotels(request):
	m_1_1 = m_hotel.objects.filter(category="m-1-1")[0:3]
	m_1_2 = m_hotel.objects.filter(category="m-1-2")[0:3]
	m_1_3 = m_hotel.objects.filter(category="m-1-3")[0:3]
	m_2_1 = m_hotel.objects.filter(category="m-2-1")[0:3]
	m_2_2 = m_hotel.objects.filter(category="m-2-2")[0:3]
	m_2_3 = m_hotel.objects.filter(category="m-2-3")[0:3]
	m_3_1 = m_hotel.objects.filter(category="m-3-1")[0:3]
	m_3_2 = m_hotel.objects.filter(category="m-3-2")[0:3]
	m_3_3 = m_hotel.objects.filter(category="m-3-3")[0:3]
	m_4_1 = m_hotel.objects.filter(category="m-4-1")[0:3]
	m_4_2 = m_hotel.objects.filter(category="m-4-2")[0:3]
	m_4_3 = m_hotel.objects.filter(category="m-4-3")[0:3]
	m_5_1 = m_hotel.objects.filter(category="m-5-1")[0:3]
	m_5_2 = m_hotel.objects.filter(category="m-5-2")[0:3]
	m_5_3 = m_hotel.objects.filter(category="m-5-3")[0:3]
	mzt = mztj.objects.all()[0:3]
	links = link.objects.all()[0:4]
	d = {"m_1_1":m_1_1,"m_1_2":m_1_2,"m_1_3":m_1_3,
	     "m_2_1":m_2_1,"m_2_2":m_2_2,"m_2_3":m_2_3,
	     "m_3_1":m_3_1,"m_3_2":m_3_2,"m_3_3":m_3_3,
	     "m_4_1":m_4_1,"m_4_2":m_4_2,"m_4_3":m_4_3,
	     "m_5_1":m_5_1,"m_5_2":m_5_2,"m_5_3":m_5_3,"mzt":mzt,"links":links}
	return TR(request,"hotel.html",d)

#注册----------------------------------------------------------------------------------------------------------------------------------------

def registers(request):
	mzt = mztj.objects.all()[0:3]
	links = link.objects.all()[0:4]
	d = {"mzt":mzt,"links":links}
	return TR(request,"register.html",d)
	
#预定联系方式提交----------------------------------------------------------------------------------------------------------------------------

def contacts(request):
	mzt = mztj.objects.all()[0:3]
	links = link.objects.all()[0:4]
	d={"mzt":mzt,"links":links}
	return TR(request,"contact.html",d)


