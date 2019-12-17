from django.db import models
from django import forms

# Create your models here.

class predicts(models.Model):
	firstname =models.CharField(max_length=15)
	info = models.TextField()
	
	def __str__(self):
	 	return self.firstname


