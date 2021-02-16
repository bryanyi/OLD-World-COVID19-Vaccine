from django.contrib import admin
from django.urls import path, include

from api.views import all_countries_vaccination_data

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', all_countries_vaccination_data.as_view(), name="api_one")
]
