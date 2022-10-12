from rest_framework import generics

from .tasks import get_data, get_file
from article.serializers import *


class ArticlesList(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesListSerializer


class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer

    def post(self, request, *args, **kwargs):
        art = int(request.data.get('art'))
        get_data.s(art=art).apply_async(countdown=3)
        return self.create(request, *args, **kwargs)


class FileCreateView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileCreateSerializer

    def post(self, request, *args, **kwargs):
        get_file.s().apply_async(countdown=2)
        return self.create(request, *args, **kwargs)
