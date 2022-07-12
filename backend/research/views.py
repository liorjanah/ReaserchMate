from rest_framework import viewsets
from .serializers import ResearchSerializer
from .models import Research


class ResearchViewSet(viewsets.ModelViewSet):
    serializer_class = ResearchSerializer
    queryset = Research.get_all()
