from django.shortcuts import render
from rest_framework import viewsets

from .serializers import order_detailsSerializer
from .models import order_details


class order_detailsViewSet(viewsets.ModelViewSet):
    queryset = order_details.objects.all().order_by('fullName')
    serializer_class = order_detailsSerializer