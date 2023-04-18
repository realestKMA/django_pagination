from django.urls import get_callable
from rest_framework.pagination import PageNumberPagination

from src.utils import api_settings, pagination
from users.models.users_model import User
from users.serializers.user_serializers import UserSerializer


class UserService:
    @staticmethod
    def list_users(request=None):
        users = User.objects.all().order_by("-date_created")

        get_paginator = get_callable(
            api_settings.get(
                "DEFAULT_PAGINATION_CLASS",
                PageNumberPagination,
            )
        )

        paginator = pagination(
            request=request,
            queryset=users,
            paginator=get_paginator,
            serializer=UserSerializer,
        )

        return paginator.data
