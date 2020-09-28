# Create your views here.
from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from .models import Register
from rest_framework import serializers
import json

class RegisterList(APIView):
    def get(self, request):
        queryset = Register.objects.all()
        serializer = RegisterSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegisterSerializer(data = request.data)         
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
