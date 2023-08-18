from django.db import models

# Create your models here.
class users(models.Model):
    firstname=models.CharField(max_length=20,null=False),
    lastname=models.CharField(max_length=20,null=False),
    phone=models.IntegerField(max_length=11,null=False),
    email=models.EmailField(null=False),
    isActive=models.BooleanField(null=False),
    isCompanyAdmin=models.BooleanField(null=False),
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class buss(models.Model):
    busType=models.CharField(null=False),
    ownerCompanyorPersonName=models.CharField(max_length=30,null=False),
    seatsNumber=models.IntegerField(null=False),
    VIP=models.BooleanField(null=False),
    isActive=models.BooleanField(null=False)
    def __str__(self):
        return f'bus ow={self.ownerCompanyorPersonName} seat={self.seatsNumber} VIP={self.VIP}'



class ticket(models.Model):
    ownerCompany=models.ForeignKey(users,on_delete=models.CASCADE),
    bus=models.ForeignKey(buss,null=True,on_delete=models.SET_NULL),
    origin=models.CharField(null=False),
    finalDestination=models.CharField(null=False),
    departureDate=models.DateField(null=False),
    departureTime=models.TimeField(null=False),
    isActive=models.BooleanField(null=False),
    price=models.IntegerField(null=False),
    def __str__(self):
        return f'ow={self.ownerCompany} ori={self.origin} des={self.finalDestination}'

