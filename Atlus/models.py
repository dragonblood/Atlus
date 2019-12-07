from django.db import models
from django import forms


class predicts(models.Model):
	firstname=models.CharField(max_length=15)
	lastname=models.CharField(max_length=15)
	info = models.TextField(null=False, blank=False)
	
	def __str__(self):
	 	return self.firstnam


