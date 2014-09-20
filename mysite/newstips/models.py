from django.db import models

class User(models.Model):
	firstname= models.CharField(max_length= 40)
	lastname= models.CharField(max_length= 40)
	username= models.CharField(max_length= 40)
	email= models.CharField(max_length= 40)
	password= models.CharField(max_length=40)
	twitter= models.CharField(max_length= 40)

class Report(models.Model):
	addressline= models.CharField(max_length= 100)
	city= models.CharField(max_length= 40)
	country= models.CharField(max_length= 2)
	state= models.CharField(max_length= 2)
	zipcode = models.CharField(max_length=10)
	time= models.DateTimeField('date publsihed')
	description= models.CharField(max_length= 1000)


class Story(models.Model):
	addressline= models.CharField(max_length= 100)
	city= models.CharField(max_length= 40)
	country= models.CharField(max_length= 2)
	state= models.CharField(max_length= 2)
	zipcode = models.CharField(max_length=10)
	time = models.DateTimeField('date occured')
	description= models.CharField(max_length= 1000)