from rest_framework import serializers
from users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор регистрации.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'phone')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            phone=validated_data.get('phone'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
