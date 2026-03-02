from django.urls import path
from .views import ProductViewClass

urlpatterns = [
    path('', ProductViewClass.as_view())
]
