from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics

from . import serializers


def healtcheck(request):
    return HttpResponse('OK!')


class SequentialCompute(generics.CreateAPIView):
    serializer_class = serializers.ComputeParams
