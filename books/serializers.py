from rest_framework import serializers

from books.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'created_at', 'updated_at')


class BookReadSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'description',
            'publication_year',
            'status',
            'notes',
            'rating',
            'authors',
            'created_at',
            'updated_at',
        )


class BookCreateSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all(), many=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'description',
            'publication_year',
            'status',
            'notes',
            'rating',
            'authors',
            'created_at',
            'updated_at',
        )
