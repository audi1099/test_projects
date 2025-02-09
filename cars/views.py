from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import CarRecord
from .serializers import CarRecordSerializer


def index(request):
    return render(request, 'cars/index.html')


def about(request):
    return HttpResponse('Обо мне')


class CarRecordViewSet(viewsets.ModelViewSet):
    queryset = CarRecord.objects.all().order_by('-date')
    serializer_class = CarRecordSerializer
