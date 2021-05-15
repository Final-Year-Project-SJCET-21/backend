from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_nested import routers

from backend_api.clasroom.api.views import (
    ClassRoomViewSet,
    EnrollViewSet,
    StudentViewset,
)

# from backend_api.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", UserViewSet)
router.register("clasroom", ClassRoomViewSet)
router.register("students", StudentViewset)
students_router = routers.NestedSimpleRouter(router, "clasroom", lookup="clasroom")
students_router.register(
    "enrolled-students", EnrollViewSet, basename="clasroom-students"
)

app_name = "api"
urlpatterns = [
    path("", include(router.urls)),
    path("", include(students_router.urls)),
]
