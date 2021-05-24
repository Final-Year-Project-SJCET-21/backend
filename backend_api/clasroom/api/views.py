# from django.db.models.query_utils import select_related_descend
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets

# from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ..models import ClassRoom, EnrolledClass, ModuleFiles, Modules
from .serializers import (
    ClassroomSerializer,
    EnrolledClassSerializer,
    ModuleFileSerializer,
    ModuleSerializer,
)


class ClassRoomViewSet(viewsets.ModelViewSet):
    """
    Rooms View
    """

    queryset = ClassRoom.objects.all().order_by("-created_on")
    serializer_class = ClassroomSerializer

    def get_queryset(self):

        # By default list of rooms return
        queryset = ClassRoom.objects.all().order_by("-created_on")
        return queryset

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        request = serializer.context["request"]
        serializer.save(created_by=request.user)

    # def destroy(self, request, pk=None):

    #     """
    #     Checks whether user requesting a delete of the room is the owner of the room or not
    #     """
    #     room = get_object_or_404(Cl, id=pk)

    #     if room:
    #         authenticate_class = JWTAuthentication()
    #         user, _ = authenticate_class.authenticate(request)
    #         if user.id == room.user.id:
    #             room.delete()
    #         else:
    #             return Response(
    #                 {
    #                     "message": "Either you are not logged in or you are not the owner of this room to delete"
    #                 },
    #                 status=status.HTTP_401_UNAUTHORIZED,
    #             )


#     return Response({}, status=status.HTTP_204_NO_CONTENT)


class EnrollViewSet(viewsets.ModelViewSet):
    serializer_class = EnrolledClassSerializer

    def get_queryset(self):
        clasroom = self.kwargs.get("clasroom_pk", None)
        queryset = EnrolledClass.objects.filter(room=clasroom)
        return queryset

    def get_serializer_class(self):
        if hasattr(self, "action") and (
            self.action == "list" or self.action == "retrieve"
        ):
            return EnrolledClassSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        room = get_object_or_404(ClassRoom, pk=self.kwargs.get("clasroom_pk"))
        if room:
            serializer.save(room=room)
            return Response(
                {"message": "This Clasroom doesnt exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response({}, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ModuleViewSet(viewsets.ModelViewSet):
    """
    Rooms View
    """

    queryset = Modules.objects.all().order_by("-created_on")
    serializer_class = ModuleSerializer

    def get_queryset(self):

        # By default list of rooms return
        queryset = Modules.objects.all().order_by("-created_on")
        return queryset

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list" or self.action == "retrieve":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        request = serializer.context["request"]
        serializer.save(created_by=request.user)


class StudentViewset(viewsets.ModelViewSet):
    queryset = EnrolledClass.objects.all()
    serializer_class = EnrolledClassSerializer


class ModuleFileVieset(viewsets.ModelViewSet):
    queryset = ModuleFiles.objects.all()
    serializer_class = ModuleFileSerializer

    def get_queryset(self):
        module = get_object_or_404(Modules, pk=self.kwargs.get("module_pk"))
        queryset = ModuleFiles.objects.filter(module=module)
        return queryset

    def perform_create(self, serializer):
        module = get_object_or_404(Modules, pk=self.kwargs.get("module_pk"))
        if module:
            serializer.save(module=module)
            return Response(
                {"message": "This module doesnt exist"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response({}, status=status.HTTP_201_CREATED)


class MyCourseViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ClassroomSerializer

    def get_queryset(self):
        if self.request.user.role == "S":
            rooms = EnrolledClass.objects.filter(student=self.request.user).values(
                "room"
            )
            return ClassRoom.objects.filter(id__in=rooms)
        return ClassRoom.objects.filter(created_by=self.request.user)
