import uuid

from django.conf import settings
from django.db import models
from django.db.models import QuerySet
from rest_framework.pagination import BasePagination
from rest_framework.request import Request
from rest_framework.serializers import Serializer

api_settings: dict = getattr(settings, "REST_FRAMEWORK", None)


class BaseModel(models.Model):
    """
    Abstract base model

    provides:

    @id = UUID4
    @date_created = DateTimeField
    @last_updated = DateTimeField
    """

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def pagination(
    request: Request,
    queryset: QuerySet,
    serializer: Serializer,
    paginator: BasePagination,
):
    """
    This util returns a paginated data.

    @params:

    :request = The api request
    :queryset = The queryset to paginate
    :paginator = Paginator class used to paginate the queryset
    :serializer = Serializer class used to serialize the paginated data
    """
    paginator = paginator()

    page = paginator.paginate_queryset(queryset=queryset, request=request)
    serializer = serializer(page, many=True)

    return paginator.get_paginated_response(serializer.data)
