from rest_framework import serializers

from ..models import ClassRoom


class ClassroomSerializer(serializers.ModelSerializer):
    # created_on = serializers.DateTimeField(
    #     format="%a %I:%M %p, %d %b %Y", read_only=True
    # )
    created_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        model = ClassRoom
        read_only_fields = ("id", "created_by", "created_on")
        fields = [
            "id",
            "room_name",
            "created_by",
            "created_on",
        ]


class EnrolledClassSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200, read_only=True)

    class Meta:
        fields = ["message"]
