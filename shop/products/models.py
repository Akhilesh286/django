from django.db import models

class ToDoList(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class details (models.Model):
  name = models.CharField(max_length=20)
class Product (models.Model):
  name = models.CharField(max_length=255)
  price = models.FloatField()
  stock = models.IntegerField()
  image = models.CharField(max_length=2500)
class offer  (models.Model):
  code = models.CharField (max_length=16)
  discription = models.CharField (max_length=255)
  discount = models.FloatField ()




# Create your models here.
