from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResearchViewSet, ResearchAssignAPI

router = DefaultRouter()
router.register(r'research', ResearchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('research/<int:pk>/assign', ResearchAssignAPI.as_view()),

]
