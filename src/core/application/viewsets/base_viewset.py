from rest_framework.viewsets import GenericViewSet
from core.application.mixins.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)


class BaseModelViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    GenericViewSet
):

    lookup_field = 'pk'
    queryset = None

    def get_queryset(self):
        return self.queryset
