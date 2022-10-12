from rest_framework import serializers

from article.models import *


class ArticlesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['art']


class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file']
