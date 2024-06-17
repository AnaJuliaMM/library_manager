from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'name', 'username', 'email', 'password']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    raise serializers.ValidationError('Esta conta está desativada.')
                data['user'] = user
            else:
                raise serializers.ValidationError('Credenciais inválidas. Tente novamente.')

        else:
            raise serializers.ValidationError('Você deve fornecer um nome de usuário e senha.')

        return data