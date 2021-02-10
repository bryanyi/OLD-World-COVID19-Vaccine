from django.contrib import admin
from django.urls import path, include

from api.views import api_one

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', api_one.as_view(), name="api_one")
]
