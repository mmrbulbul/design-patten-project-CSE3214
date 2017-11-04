from __future__ import unicode_literals
from datetime import datetime

from django.db import models

# Create your models here.
# Create your models here.
class CategoryModel(models.Model):
	category = models.CharField(max_length = 30, unique=True)

	def __str__(self):
		return self.category

class LocationModel(models.Model):
	location = models.CharField(max_length = 30, unique=True)

	def __str__(self):
		return self.location


class Rental(models.Model):
	location = models.ForeignKey('LocationModel', default = '', on_delete=models.CASCADE)
	rent = models.IntegerField()
	advance = models.IntegerField(blank=True,null=True)
	contact = models.CharField(max_length=17)
	details = models.TextField(max_length=200,blank=True,null=True)
	available_from = models.DateField()
	available_upto = models.DateField(null=True, blank=True)
	posted_on = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		i = str(self.id)
		s = str(self.rent)
		l = str(self.location)
		return  "Rental " + i + " with" + s + " sq. feet apartment at " + l 

class Apartment(Rental):
	size = models.IntegerField()
	parking_space = models.BooleanField()
	no_of_bed = models.IntegerField()
	no_of_bath = models.IntegerField()
	floor_no = models.IntegerField()
	lift = models.BooleanField()
	cctv = models.BooleanField()
	generator = models.BooleanField()
	balcony = models.BooleanField()
	service_charge = models.IntegerField(default=0)


class Hostel(Rental):
	no_of_roommate = models.IntegerField()
	available_roommate = models.IntegerField()
	rent_with_meal = models.IntegerField(null=True, blank=True)
	bed = models.BooleanField()
	table = models.BooleanField()
	chair = models.BooleanField()
	water_purifier = models.BooleanField()

class ConventionCentre(Rental):
	name = models.CharField(max_length=35,blank=True,null=True)
	size_of_floor = models.IntegerField()
	no_of_floor = models.IntegerField()
	human_capacity = models.IntegerField()
	catering_system = models.BooleanField()
	parking_space = models.IntegerField()
	open_space = models.BooleanField()

class Sublet(Rental):
	total_roommate = models.IntegerField()
	available_roommate = models.IntegerField()
	family = models.BooleanField()
	bed = models.BooleanField()
	table = models.BooleanField()
	chair = models.BooleanField()
	water_purifier = models.BooleanField()

class Garage(Rental):
	a = "nothing"

class Office(Rental):
	size = models.IntegerField()





	
		