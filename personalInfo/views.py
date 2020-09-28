from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import PersonalInfoSerializer
from .models import PersonalInfo
# Create your views here.
class PersonalInfoList(APIView):
    def get(self, request):
        queryset = PersonalInfo.objects.all()
        serializer = PersonalInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonalInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonalInfoDetails(APIView):
    def get_object(self, pk):
        try:
            return PersonalInfo.objects.get(pk=pk)
        except PersonalInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        personalinfo = self.get_object(pk)
        serializer = PersonalInfoSerializer(personalinfo)
        return Response(serializer.data)