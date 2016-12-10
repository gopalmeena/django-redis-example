from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Country(models.Model):
	country_id=models.AutoField(primary_key=True)
	name=models.TextField(blank=False)
	code=models.CharField(max_length=100,unique=True)

class State(models.Model):
	state_id=models.AutoField(primary_key=True)
	name=models.TextField(blank=False)
	code=models.CharField(max_length=100,unique=True)
	country = models.ForeignKey(Country)

class City(models.Model):
	city_id=models.AutoField(primary_key=True)
	name=models.TextField(blank=False)
	code = models.CharField(max_length=100,unique=True)
	state = models.ForeignKey(State)