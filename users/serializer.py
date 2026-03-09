from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User


class CustumTokenObtainPairSerialize(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Ajouter des infos dans la RÉPONSE
        data["user"] = { # type: ignore
            "id": self.user.id, # type: ignore
            "username": self.user.username, # type: ignore
            "email": self.user.email, # type: ignore
            "is_staff": self.user.is_staff, # type: ignore
        }

        return data

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"