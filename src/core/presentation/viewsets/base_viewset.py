from rest_framework.viewsets import GenericViewSet


class BaseViewSet(
    GenericViewSet
):

    lookup_field = 'pk'
    queryset = None

    def get_queryset(self):
        return self.queryset
