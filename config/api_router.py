from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from backend_api.clasroom.api.views import ClassRoomViewSet

# from backend_api.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", UserViewSet)
router.register("clasroom", ClassRoomViewSet)


app_name = "api"
urlpatterns = router.urls
