from django.shortcuts import render
from django.http import JsonResponse
from .models import covidVaccinationData

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import covidVaccinationDataSerializer

class most_vaccinated(APIView):
    def get(self, request, *args, **kwargs):
        mySQL="""
            SELECT *
            FROM api_covidvaccinationdata
            WHERE total_vaccinations IN (
	        SELECT MAX(total_vaccinations)
            FROM api_covidvaccinationdata
            )
            """
        
        querySet = covidVaccinationData.objects.raw(mySQL)
    
        serializer = covidVaccinationDataSerializer(querySet, many=True)
        return Response(serializer.data)

class all_countries_vaccination_data(APIView):
    
    def get(self, request, *args, **kwargs):
        
        mySQL = """
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Algeria'
            ) && country = 'Algeria'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Andorra'
            ) && country = 'Andorra'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Argentina'
            ) && country = 'Argentina'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Austria'
            ) && country = 'Austria'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Bahrain'
            ) && country = 'Bahrain'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Argentina'
            ) && country = 'Argentina'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Bangladesh'
            ) && country = 'Bangladesh'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Belgium'
            ) && country = 'Belgium'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Bermuda'
            ) && country = 'Bermuda'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Bolivia'
            ) && country = 'Bolivia'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Brazil'
            ) && country = 'Brazil'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Bulgaria'
            ) && country = 'Bulgaria'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Canada'
            ) && country = 'Canada'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Cayman Islands'
            ) && country = 'Cayman Islands'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Chile'
            ) && country = 'Chile'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'China'
            ) && country = 'China'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Costa Rica'
            ) && country = 'Costa Rica'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Croatia'
            ) && country = 'Croatia'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Cyprus'
            ) && country = 'Cyprus'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Czechia'
            ) && country = 'Czechia'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Denmark'
            ) && country = 'Denmark'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Ecuador'
            ) && country = 'Ecuador'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Egypt'
            ) && country = 'Egypt'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'England'
            ) && country = 'England'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Estonia'
            ) && country = 'Estonia'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Faeroe Islands'
            ) && country = 'Faeroe Islands'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Finland'
            ) && country = 'Finland'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'France'
            ) && country = 'France'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Germany'
            ) && country = 'Germany'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Gibraltar'
            ) && country = 'Gibraltar'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Greece'
            ) && country = 'Greece'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Greenland'
            ) && country = 'Greenland'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Guernsey'
            ) && country = 'Guernsey'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Hungary'
            ) && country = 'Hungary'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Iceland'
            ) && country = 'Iceland'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'India'
            ) && country = 'India'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Indonesia'
            ) && country = 'Indonesia'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Ireland'
            ) && country = 'Ireland'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Isle of Man'
            ) && country = 'Isle of Man'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Israel'
            ) && country = 'Israel'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Italy'
            ) && country = 'Italy'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Jersey'
            ) && country = 'Jersey'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Kuwait'
            ) && country = 'Kuwait'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Lativa'
            ) && country = 'Lativa'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Liechtenstein'
            ) && country = 'Liechtenstein'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Lithuania'
            ) && country = 'Lithuania'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Luxembourg'
            ) && country = 'Luxembourg'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Maldives'
            ) && country = 'Maldives'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Malta'
            ) && country = 'Malta'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Mexico'
            ) && country = 'Mexico'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Monaco'
            ) && country = 'Monaco'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Morocco'
            ) && country = 'Morocco'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Myanmar'
            ) && country = 'Myanmar'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Nepal'
            ) && country = 'Nepal'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Netherlands'
            ) && country = 'Netherlands'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Northern Cyprus'
            ) && country = 'Northern Cyprus'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Northern Ireland'
            ) && country = 'Northern Ireland'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Norway'
            ) && country = 'Norway'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Oman'
            ) && country = 'Oman'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Panama'
            ) && country = 'Panama'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Poland'
            ) && country = 'Poland'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Portugal'
            ) && country = 'Portugal'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Romania'
            ) && country = 'Romania'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Russia'
            ) && country = 'Russia'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Saint Helena'
            ) && country = 'Saint Helena'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Russia'
            ) && country = 'Russia'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Saint Helena'
            ) && country = 'Saint Helena'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Saudi Arabia'
            ) && country = 'Saudi Arabia'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Scotland'
            ) && country = 'Scotland'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Serbia'
            ) && country = 'Serbia'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Seychelles'
            ) && country = 'Seychelles'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Singapore'
            ) && country = 'Singapore'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Slovakia'
            ) && country = 'Slovakia'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Slovenia'
            ) && country = 'Slovenia'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Spain'
            ) && country = 'Spain'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Sri Lanka'
            ) && country = 'Sri Lanka'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Sweden'
            ) && country = 'Sweden'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Switzerland'
            ) && country = 'Switzerland'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Turkey'
            ) && country = 'Turkey'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'United Arab Emirates'
            ) && country = 'United Arab Emirates'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'United Kingdom'
            ) && country = 'United Kingdom'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'United States'
            ) && country = 'United States'
            UNION
            SELECT *
            FROM WD_covid_vaccination_project_data_1
            WHERE date = (
                SELECT MAX(date) FROM WD_covid_vaccination_project_data_1 WHERE country = 'Wales'
            ) && country = 'Wales'

            """
        
        querySet = covidVaccinationData.objects.raw(mySQL)
    
        serializer = covidVaccinationDataSerializer(querySet, many=True)
        return Response(serializer.data)
        
