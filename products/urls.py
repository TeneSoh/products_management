from django.urls import path, include
# from .views import ProductViewClass, ProductId
from .views import ProductViewClass
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'product', ProductViewClass, basename='products')

urlpatterns = [
    # path('', ProductViewClass.as_view()),
    path('', include(router.urls)),
    # path('product/<int:pk>/', ProductId.as_view()),
]
