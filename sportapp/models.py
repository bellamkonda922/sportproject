from django.db import models
from django.urls import reverse
# Create your models here.


import uuid


class clubs(models.Model):
    name = models.CharField(max_length=30,help_text='Enter a club name')
    secy_name= models.CharField(max_length=30,help_text='Enter a secy name')
    email=  models.EmailField()
    dept=models.CharField(max_length=40,help_text='Department')
    prog=models.CharField(max_length=50,help_text='Programme')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('clubsList')    

class equipment(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular equipment')
    name = models.CharField(max_length=30)
    total_quantity= models.IntegerField(null=True)
    available_quantity=models.IntegerField(null=True)
    sport= models.ForeignKey('clubs', on_delete=models.CASCADE)
    specification=models.TextField(null=True)
    date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name      

class issue(models.Model):
    equipment_name= models.ForeignKey('equipment',on_delete=models.CASCADE, null=True)
    roll= models.CharField(max_length=30) 
    name=  models.CharField(max_length=50)
    quantity= models.PositiveIntegerField(null=True)
    date= models.DateTimeField(auto_now=True)
    is_return= models.BooleanField(default=False)
    is_pending= models.BooleanField(default=True)
    req=models.BooleanField(default=False)
    remark=models.TextField(null=True)
    class Meta:
        ordering = ['date']
class generalequipment(models.Model):
    name = models.CharField(max_length=30)
    total_quantity= models.IntegerField(null=True)
    available_quantity=models.IntegerField(null=True)
    specification=models.TextField(null=True)
    date=models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.name    
