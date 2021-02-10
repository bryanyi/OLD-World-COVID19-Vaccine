from rest_framework import serializers
from .models import covidVaccinationData

class covidVaccinationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = covidVaccinationData
        fields = (
            'country',
            'vaccinated',
            'comments'
        )