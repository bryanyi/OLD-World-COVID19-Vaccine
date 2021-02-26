from django.contrib import admin
from django.urls import path, include, re_path

from api.views import all_countries_vaccination_data, most_vaccinated, FrontendAppView
from django.views.generic import TemplateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', all_countries_vaccination_data.as_view(), name="all_countries_vaccination_data"),
    path('most-vaccinated/', most_vaccinated.as_view(), name="most_vaccinated"),
    re_path(r'^', views.FrontendAppView.as_view()),
]
