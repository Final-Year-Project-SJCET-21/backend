from rest_framework import serializers

from ..models import ClassRoom,Modules


class ClassroomSerializer(serializers.ModelSerializer):
    # created_on = serializers.DateTimeField(
    #     format="%a %I:%M %p, %d %b %Y", read_only=True
    # )
    created_by = serializers.StringRelatedField(
        default=serializers.CurrentUserDefault(), read_only=True
    )

    class Meta:
        model = ClassRoom
        read_only_fields = ("created_by", "created_on")
        fields = [
            "id",
            "room_name",
            "created_by",
            "created_on",
        ]
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        read_only_fields = ( "created_on") 
        fields = [
            "module_name",
            "room",
            "created_on",
        ]
            