from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class foodModel(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    quantity=models.FloatField()
    protein=models.FloatField()
    carbs=models.FloatField()
    fat=models.FloatField()
    nutrients=models.FloatField()
    vitamins=models.CharField(max_length=100)
    foodimg=models.ImageField(upload_to="fimage/",blank=True)
    fav=models.ManyToManyField(User,related_name='favs',blank=True,default=False)

    def __str__(self):
        return self.name
    

    
class dailycalory(models.Model):
    dname=models.CharField(max_length=100)
    dtype=models.CharField(max_length=100)
    dquantity=models.FloatField()
    dprotein=models.FloatField()
    dcarbs=models.FloatField()
    dfat=models.FloatField()
    dnutrients=models.FloatField()
    dvitamins=models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  self.dname
    
    class Meta:
        ordering = ['-updated_at']
    
    

