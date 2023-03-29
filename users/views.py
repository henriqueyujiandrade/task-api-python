from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from .models import User
import ipdb
from .serializers import UserSerializer

class UserRegisterView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class LoginView(ObtainAuthToken):
    
    def post(self, request: Request) -> Response:
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            "user": {
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name
            },
            "token": token.key
            })