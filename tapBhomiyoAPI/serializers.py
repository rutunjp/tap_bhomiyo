from rest_framework import serializers

from .models import order_details

class order_detailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = order_details
        fields = ('fullName', 'email','phone',
'aadhar',
'panNum',
'postalAddress',
'upiID',
'whatsAppNumber',
'instagramHandle', 
'twitterHandle',
'facebookHandle',
'youtube',
'linkedIn',
'referenceCode',
'birthDate')