# from base_user.models import BaseUser
# from rest_framework import generics, permissions
from rest_framework import generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import BaseUserSerializer, LoginSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = BaseUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        base_user = serializer.save()
        _, token = AuthToken.objects.create(base_user.user)
        return Response({
            "user": BaseUserSerializer(base_user,
                                       context=self.get_serializer_context()).data,
            "token": token
        })


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": BaseUserSerializer(user.baseuser, context=self.get_serializer_context()).data,
            "token": token
        })
