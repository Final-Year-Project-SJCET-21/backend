from rest_framework import serializers

from backend_api.users.api.serializers import UserDetailSerializer

from ..models import ClassRoom, EnrolledClass, ModuleFiles, Modules


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


class EnrolledClassSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.name", read_only=True)

    class Meta:
        model = EnrolledClass
        read_only_fields = ["room", "student_name"]
        fields = ["room", "student_name"]


class EnrollViewSerializer(serializers.Serializer):
    room = ClassroomSerializer(many=False)
    students = UserDetailSerializer(source="student", many=True)

    # class Meta:
    #     model = EnrolledClass
    #     fields = ["room"]
    #


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        read_only_fields = ["id", "room", "created_on"]
        fields = [
            "id",
            "module_name",
            "room",
            "created_on",
        ]


class ModuleFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleFiles
        fields = ["module", "filename", "document", "description"]
