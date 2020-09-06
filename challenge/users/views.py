from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions
from rest_framework.settings import api_settings
from users import serializers


class UserLoginApiView(ObtainAuthToken):
    """ Enables the login API view and retrieves a token
        for authentication """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UsersRegistrationApiView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')
            token = create_and_authenticate_user(username, password)
            return Response({
                'user': serializer.data,
                'token': token.key
            },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def create_and_authenticate_user(username, password):
    """ Creates a user on the database and returns
        its token for authorization """

    user = create_user(username, password)

    token = get_user_token(user)
    return token


def create_user(username, password):
    user = User.objects.create(
        username=username,
        password=password
    )
    user.set_password(password)
    user.save()
    return user


def get_user_token(user=None):
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return token
    return None
