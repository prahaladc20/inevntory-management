from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Inventory(models.Model):
	author 			=	models.ForeignKey(User, on_delete=models.CASCADE)
	product_id 		= 	models.AutoField(null=False,primary_key=True)
	product_name 	= 	models.CharField(max_length=200)
	vendor 			= 	models.CharField(max_length=200)
	mrp 			= 	models.FloatField(max_length=10)
	batch_num		= 	models.IntegerField()
	batch_date 		=	models.DateField()
	quantity 		= 	models.IntegerField()
	status 			= 	models.IntegerField()

	def __str__(self):
		return self.product_name
	        