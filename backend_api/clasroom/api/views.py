from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..models import ClassRoom
from .serializers import ClassroomSerializer, EnrolledClassSerializer


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


class EnrollViewSet(generics.CreateAPIView):
    serializer_class = EnrolledClassSerializer
