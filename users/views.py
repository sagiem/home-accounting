from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from users import serializers
from users import models


class RegisterUser(GenericAPIView):
    queryset = models.CustomUser
    serializer_class = serializers.RegisteUser

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = models.CustomUser.objects.create_user(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password'],
        )
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=201)


class LoginUser(GenericAPIView):
    queryset = models.CustomUser
    serializer_class = serializers.LoginUser

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = Token.objects.get(user__username=serializer.validated_data['username'])
        return Response({'token': token.key})


