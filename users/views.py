from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .serializer import Userserializer, CustumTokenObtainPairSerialize
from rest_framework.response import Response
from rest_framework import status



class CustumTokenObtainPairView(TokenObtainPairView):
    serialize_class = CustumTokenObtainPairSerialize

# Create your views here.
class CreatUser(APIView):
    def post(self, request):
        serializer = Userserializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                'data':serializer.data,
            },status= status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)