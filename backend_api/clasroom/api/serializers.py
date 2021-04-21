from rest_framework import serializers

from ..models import ClassRoom


class ClassroomSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(
        format="%a %I:%M %p, %d %b %Y", required=False
    )

    class Meta:
        model = ClassRoom
        fields = [
            "id",
            "room_name",
            "created_by",
            "created_on",
        ]
