from django.urls import path
from .views import ParticipantRegisterAPI, ParticipantAPI

urlpatterns = [
    path('participant/register', ParticipantRegisterAPI.as_view()),
    path('participant/<int:pk>', ParticipantAPI.as_view()),
]
