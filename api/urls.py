from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    api_home
)

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', api_home), # localhost:8000/api/
    path('search/', include('search.urls')),
    path('products/', include('products.urls')),
    path('articles/', include('articles.api_urls')),
]
