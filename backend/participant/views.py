from rest_framework import generics
from rest_framework.response import Response
from .serializers import ParticipantSerializer


class ParticipantRegisterAPI(generics.GenericAPIView):
    serializer_class = ParticipantSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()
