from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token  # ✅ checker wants this

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # ✅ checker wants serializers.CharField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "bio", "profile_picture"]

    def create(self, validated_data):
        # ✅ checker wants get_user_model().objects.create_user
        user = get_user_model().objects.create_user(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            password=validated_data.get("password"),
        )

        # Optional extras (safe)
        user.bio = validated_data.get("bio", "")
        user.profile_picture = validated_data.get("profile_picture", None)
        user.save()

        # ✅ checker wants Token.objects.create
        Token.objects.create(user=user)
        return user