from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.CharField(source="actor.username", read_only=True)

    class Meta:
        model = Notification
        fields = [
            "id",
            "actor",
            "actor_username",
            "verb",
            "timestamp",
            "is_read",
            "target_object_id",
        ]
        read_only_fields = fields