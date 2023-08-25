from django.db import models

# Create your models here.
class users(models.Model):
    firstname=models.CharField(max_length=20,null=False,default="0")
    lastname=models.CharField(max_length=20,null=False,default="0")
    phone=models.IntegerField(null=False,default=0)
    email=models.EmailField(null=False,default="0")
    isActive=models.BooleanField(null=False,default=False)
    isCompanyAdmin=models.BooleanField(null=False,default=False)
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class buss(models.Model):
    busType=models.CharField(max_length=30,null=False,default="0")
    ownerCompanyorPersonName=models.CharField(max_length=30,null=False,default="0")
    seatsNumber=models.IntegerField(null=False,default=0)
    VIP=models.BooleanField(null=False,default=False)
    isActive=models.BooleanField(null=False,default=False)
    def __str__(self):
        return f'bus ow={self.ownerCompanyorPersonName} seat={self.seatsNumber} VIP={self.VIP}'


class ticket(models.Model):
    ownerCompany=models.ForeignKey(users,on_delete=models.CASCADE,default="0")
    bus=models.ForeignKey(buss,null=True,on_delete=models.SET_NULL,default="0")
    origin=models.CharField(max_length=30,null=False,default="0")
    finalDestination=models.CharField(max_length=30,null=False,default="0")
    departureDate=models.DateField()
    departureTime=models.TimeField()
    isActive=models.BooleanField(null=False,default=False)
    price=models.IntegerField(null=False,default=False)
    def __str__(self):
        return f'ow={self.ownerCompany} ori={self.origin} des={self.finalDestination}'


class destinations(models.Model):
    destName=models.CharField(max_length=30,null=False,default="0")
    ticket=models.ForeignKey(ticket,on_delete=models.CASCADE,default="0")

class boughtTickets(models.Model):
    ownerUser=models.ForeignKey(users,null=True,on_delete=models.SET_NULL,default="0")
    ticket=models.ForeignKey(ticket,null=True,on_delete=models.SET_NULL,default="0")