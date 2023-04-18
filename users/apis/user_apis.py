from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from users.models.users_model import User
from users.serializers.user_serializers import UserSerializer
from users.services.user_services import UserService


class ListUserAPI1(generics.GenericAPIView):
    pagination_class = PageNumberPagination

    def get(self, request):
        return Response(
            data=UserService.list_users(request=request),
            status=status.HTTP_200_OK,
        )


class ListUserAPI2(generics.GenericAPIView, ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@api_view(["GET"])
def ListUserAPI3(request):
    pagination_class = PageNumberPagination
    paginator = pagination_class()
    queryset = User.objects.all()
    page = paginator.paginate_queryset(queryset, request)

    serializer = UserSerializer(page, many=True)

    return paginator.get_paginated_response(serializer.data)
