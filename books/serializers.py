from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Book
        fields = ['id', 'url', 'title', 'synopsis', 'cover', 'author']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True, view_name='book-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'books']
