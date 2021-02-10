from django.shortcuts import render
from django.http import JsonResponse

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import covidVaccinationDataSerializer
from .models import covidVaccinationData

class api_one(APIView):
    def get(self, request, *args, **kwargs):
        querySet = covidVaccinationData.objects.all()
        serializer = covidVaccinationDataSerializer(querySet, many=True)
        return Response(serializer.data)
        

    def post(self, request, *args, **kwargs):
        serializer = covidVaccinationDataSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)