from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PersonSerializer
from .models import Person

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

