from django.db import models
from PIL import Image
#import numpy as np

from django.contrib.auth.models import User
from django import forms
import os
from django.urls import reverse
from datetime import datetime

# Create your models here.



types =(('','Select Type'),('Primary','Primary'),('Secondary','Secondary'))
class UserRegistration(models.Model):
	
	profile_pic = models.ImageField(upload_to= "User_Portal/profiles",blank=True)

	first_name = models.CharField(max_length=80)
	
	last_name = models.CharField(max_length=80)
	
	mobile_number= models.CharField(max_length=122)
		
	email= models.CharField(max_length=122)
	
	gender = models.CharField(max_length=122)
	birthdate = models.DateField()
	type = models.CharField(max_length=122,choices=types)
	
	class Meta:
		db_table= "BombaySoftwares_user_registration"
		
	def __str__(self):
		return self.first_name 
	
