from django.shortcuts import render
from django.http import JsonResponse
from .models import covidVaccinationData

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import covidVaccinationDataSerializer

class api_one(APIView):
    def get(self, request, *args, **kwargs):
        # querySet = covidVaccinationData.objects.all()
        
        mySQL = """
            
            SELECT *  
            FROM VaccinationData.WD_covid_vaccination_project_data_1 
            WHERE country='Andorra'
            
            """
        
        querySet = covidVaccinationData.objects.raw(mySQL)
    
        serializer = covidVaccinationDataSerializer(querySet, many=True)
        return Response(serializer.data)
        
