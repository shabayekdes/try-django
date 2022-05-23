from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
    api_home
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', api_home), # localhost:8000/api/
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('search/', include('search.urls')),
    path('products/', include('products.urls')),
    path('articles/', include('articles.api_urls')),
]

