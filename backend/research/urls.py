from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ResearchViewSet

router = DefaultRouter()
router.register(r'research', ResearchViewSet)

urlpatterns = [
    path('', include(router.urls))
]
