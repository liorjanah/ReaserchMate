from rest_framework import viewsets
from .serializers import ParticipantSerializer
from .models import Participant


class ParticipantViewSet(viewsets.ModelViewSet):
    serializer_class = ParticipantSerializer
    queryset = Participant.get_all()
