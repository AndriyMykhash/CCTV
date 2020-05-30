from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serialisers import MyTokenObtainPairSerializer, UserSerializer, User


class ObtainTokenPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(True):
            user = serializer.save()
            user.save_base()
            token_refresh = MyTokenObtainPairSerializer().get_token(user)
            token_access = AccessToken().for_user(user)
            response = {
                'message': 'User registered  successfully',
                'tokens': {
                    "refresh": str(token_refresh),
                    "access": str(token_access)
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
