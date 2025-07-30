from rest_framework.viewsets import GenericViewSet
from core.presentation.mixins.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
)


class BaseModelViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    GenericViewSet
):

    lookup_field = 'pk'
    queryset = None

    def get_queryset(self):
        return self.queryset
