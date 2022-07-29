from django.urls import path
from .views import ParticipantRegisterAPI

urlpatterns = [
    path('participant/register', ParticipantRegisterAPI.as_view()),
]
