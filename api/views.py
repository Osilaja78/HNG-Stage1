from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MyDetailsSerializer
from .models import MyDetails

# Create your views here.
class MyDetailsViewSet(viewsets.ModelViewSet):
    queryset = MyDetails.objects.all()
    serializer_class = MyDetailsSerializer
