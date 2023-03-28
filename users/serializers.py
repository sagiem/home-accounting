from rest_framework import serializers
from users import models



class RegisteUser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)


    def validate_username(self, value):
        if models.CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError('Пользователь с таким именем уже есть')
        return value

class LoginUser(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(min_length=8)

    def validate_username(self, value):
        if not models.CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError('Пользователь с таким именем не найден')
        return value

    def validate(self, attrs):
        user = models.CustomUser.objects.get(username=attrs['username'])
        if not user.check_password(attrs['password']):
            raise serializers.ValidationError({'password': 'Не верный пароль'})
        return attrs