from typing import Type

from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from books.models import Book, Author
from books.serializers import BookReadSerializer, AuthorSerializer, BookCreateSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.prefetch_related('authors').all()
    serializer_class = BookReadSerializer

    def get_serializer_class(self) -> Type[BookReadSerializer | BookCreateSerializer]:
        if self.action in ['list', 'retrieve', 'top']:
            return BookReadSerializer
        return BookCreateSerializer

    @action(detail=False, methods=['get'])
    def top(self, request: Request) -> Response:
        books = self.get_queryset().order_by('-created_at', '-rating')[:3]
        serializer = self.get_serializer(books, many=True)

        return Response(serializer.data)


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
