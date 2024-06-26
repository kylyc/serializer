from django.shortcuts import render
from rest_framework import generics
from .serializer import WomenSerializer

from .models import Women
# Create your views here.


class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer