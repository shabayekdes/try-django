from django.urls import path, include

from .views import (
    api_home
)

urlpatterns = [
    path('', api_home), # localhost:8000/api/
    path('products/', include('products.urls'))
]
