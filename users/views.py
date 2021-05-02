from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import User
from .permissions import IsAdminOrOwner
from .serializers import UserSerializer, UserSerializerNoRole


class UserListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrOwner, ]
    pagination_class = PageNumberPagination
    queryset = User.objects.all()
    lookup_field = 'username'

    def get_serializer_class(self):
        if self.request.method == 'PATCH' and not self.request.user.is_admin:
            return UserSerializerNoRole
        return UserSerializer

    @action(detail=False, methods=['GET', 'PATCH'])
    def me(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PATCH':
            if user.is_admin:
                serializer = UserSerializer(
                    user,
                    data=request.data,
                    partial=True
                )
            else:
                serializer = UserSerializerNoRole(
                    user,
                    data=request.data,
                    partial=True
                )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
