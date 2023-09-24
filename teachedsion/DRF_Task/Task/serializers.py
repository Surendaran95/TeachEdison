from rest_framework import serializers
from .models import Author, Magazine, Article

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class MagazineDetailSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

class AuthorDetailSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
