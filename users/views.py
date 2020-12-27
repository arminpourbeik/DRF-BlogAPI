from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import RegisterUserSerializer


class CustomUserCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)

        if serializer.is_valid():
            new_user = serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)

            return Response(
                serializer.errors, status=status.status.HTTP_400_BAD_REQUEST
            )
