from typing import TypeVar, Generic, Any
from rest_framework.response import Response
from rest_framework import status

T = TypeVar('T')
ID = TypeVar('ID')


class BaseServiceMixin(Generic[T, ID]):
    service: Any  # Будет заменен конкретным сервисом

    def get_entity(self, entity_id: ID) -> T:
        raise NotImplementedError

    def get_all_entities(self) -> list[T]:
        raise NotImplementedError

    def create_entity(self, data: dict) -> T:
        raise NotImplementedError

    def update_entity(self, entity_id: ID, data: dict) -> T:
        raise NotImplementedError

    def delete_entity(self, entity_id: ID) -> None:
        raise NotImplementedError


class RetrieveModelMixin(BaseServiceMixin[T, ID]):

    def retrieve(self, request, *args, **kwargs) -> Response:
        try:
            entity = self.get_entity(kwargs['pk'])
            serializer = self.get_serializer(entity)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_404_NOT_FOUND
            )


class ListModelMixin(BaseServiceMixin[T, ID]):

    def list(self, request, *args, **kwargs) -> Response:
        entities = self.get_all_entities()
        serializer = self.get_serializer(entities, many=True)
        return Response(serializer.data)


class CreateModelMixin(BaseServiceMixin[T, ID]):

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        entity = self.create_entity(serializer.validated_data)
        serializer = self.get_serializer(entity)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class UpdateModelMixin(BaseServiceMixin[T, ID]):
    def update(self, request, *args, **kwargs) -> Response:
        try:
            entity = self.update_entity(
                entity_id=kwargs['pk'],
                data=request.data
            )
            serializer = self.get_serializer(entity)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_404_NOT_FOUND
            )


class DestroyModelMixin(BaseServiceMixin[T, ID]):

    def destroy(self, request, *args, **kwargs) -> Response:
        try:
            self.delete_entity(kwargs['pk'])
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_404_NOT_FOUND
            )
