from django.db import models
from django.core.validators import MinLengthValidator 
from phonenumber_field.modelfields import PhoneNumberField
class order_details(models.Model):
    fullName=models.CharField(max_length=100)
    email=models.EmailField
    phone=PhoneNumberField()
    aadhar= models.CharField(max_length=12, validators=[MinLengthValidator(12)])
    panNum= models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    postalAddress=models.CharField(max_length=255)
    upiID=models.CharField(max_length=20)
    whatsAppNumber= PhoneNumberField()
    instagramHandle=models.CharField(max_length=30, null=True)
    twitterHandle=models.CharField(max_length=30, null=True)
    facebookHandle=models.CharField(max_length=30, null=True)
    youtube=models.CharField(max_length=30, null=True)
    linkedIn=models.CharField(max_length=30, null=True)
    referenceCode=models.CharField(max_length=5, null=True)
    birthDate=models.DateField()
