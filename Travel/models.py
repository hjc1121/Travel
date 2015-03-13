from django.db import models
from datetime import datetime

#index-----------------------------------------------------------------
class Image(models.Model):
	img = models.ImageField(upload_to='./img')

class home(models.Model):
	name1 = models.CharField(max_length=30)
	name2 = models.CharField(max_length=30)
	name3 = models.CharField(max_length=30)
	text11 = models.TextField()
	text12 = models.TextField()
	text13 = models.TextField()
	text21 = models.TextField()
	text22 = models.TextField()
	text23 = models.TextField()
	text31 = models.TextField()
	text32 = models.TextField()
	text33 = models.TextField()
	img1 = models.ImageField(upload_to = "./img")
	img2 = models.ImageField(upload_to = "./img")
	img3 = models.ImageField(upload_to = "./img")
	date = models.DateTimeField(default=datetime.now(),blank=True)

class visions(models.Model):
	name = models.CharField(max_length=30)
	text = models.TextField()
	img = models.ImageField(upload_to = "./img")


class record(models.Model):
	name = models.CharField(max_length=30)
	title = models.CharField(max_length=50)
	category = models.CharField(max_length=30) 
	img = models.ImageField(upload_to = "./img")
	text = models.TextField()


class feature(models.Model):
	name = models.CharField(max_length=30)
	title = models.CharField(max_length=30)
	img = models.ImageField(upload_to = "./img")
#fea-index-1-----------------------------------------------------------

class fea_index1(models.Model):
	name = models.CharField(max_length=60)
	img = models.ImageField(upload_to = "./img")
	text = models.TextField()

class fea_history(models.Model):
	img = models.ImageField(upload_to = "./img")
	text = models.TextField()
	date = models.TextField(max_length=15)

class fea_place(models.Model):
	name = models.CharField(max_length=60)
	text = models.TextField()

#WKfeature---------------------------------------------------------------

class YDt(models.Model):
	title = models.CharField(max_length=30)
	title2 = models.CharField(max_length=50)
	category = models.CharField(max_length=30)
	categoryid = models.CharField(max_length=80)
	img = models.ImageField(upload_to = "./img")
	text = models.TextField()

		


#fotter-----------------------------------------------------------------

class mztj(models.Model):
	name = models.CharField(max_length=30)
	img = models.ImageField(upload_to = "./img")
	text = models.TextField()
	date = models.DateTimeField(default=datetime.now(),blank=True)

class link(models.Model):
	name = models.CharField(max_length=30)
	img = models.ImageField(upload_to = "./img")
	src = models.TextField()
	

#photos------------------------------------------------------------------

class xiangce(models.Model):
	name = models.CharField(max_length=30)
	place = models.CharField(max_length=50)
	view = models.CharField(max_length=100)
	visitor = models.CharField(max_length=30)
	img1 = models.ImageField(upload_to="./img")
	img2 = models.ImageField(upload_to="./img")
	date = models.DateTimeField(default=datetime.now(),blank=True)

#visitor------------------------------------------------------------------

class m_visitors(models.Model):
	name = models.CharField(max_length=50)
	title = models.CharField(max_length=20)
	text =  models.TextField()
	colors = models.TextField()
	img = models.ImageField(upload_to='./img')

#hotel--------------------------------------------------------------------

class m_hotel(models.Model):
	name = models.CharField(max_length=30)
	category = models.CharField(max_length=30) 
	img = models.ImageField(upload_to = "./img")
	text = models.TextField()

		