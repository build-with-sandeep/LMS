from rest_framework import serializers
from .models import Librarian, Member, Book

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Librarian
        fields = ['username', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        librarian = Librarian(**validated_data)
        librarian.set_password(password)
        librarian.save()
        return librarian

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['username', 'name', 'email', 'password', 'registration_time']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        member = Member(**validated_data)
        member.set_password(password)
        member.save()
        return member

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'status', 'cover_image', 'pdf_file', 'borrower']
        read_only_fields = ['id', 'status', 'borrower']
