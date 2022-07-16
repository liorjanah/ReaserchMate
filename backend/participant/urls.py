from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParticipantViewSet

router = DefaultRouter()
router.register(r'participant', ParticipantViewSet)

urlpatterns = [
    path('', include(router.urls))
]
