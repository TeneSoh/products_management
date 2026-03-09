from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import CustumTokenObtainPairView, CreatUser

urlpatterns = [
    path('', CreatUser.as_view(), name='create_user'),
    path('login/', CustumTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh_token'),
]
