from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UsersListSerializer(serializers.Serializer):
    # Actúa como un traductor de objetos a tipos primitivos (lo contrario a lo que hace un formulario)
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserSerializer(UsersListSerializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_username(self, data):
        # if User.objects.filter(username=data).exists():
        if self.instance is None and User.objects.filter(username=data).exists():
            # La primera condición se cumple cuando se está creando un usuario
            raise ValidationError("El usuario ya existe")
        if self.instance and self.instance.username == data and User.objects.filter(username=data).exists():
            raise ValidationError("Este nombre de usuario ya existe")
        return data

    def create(self, validated_data):  # Construye un objeto User
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.set_password(validated_data.get("password"))
        # El método "set_password" cifra la contraseña
        instance.save()
        return instance


