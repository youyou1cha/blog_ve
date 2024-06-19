from rest_framework import viewsets

from .filters import ArticleFilter
from .models import Article, Avater, Category, Tag
from .permissions import IsAdminUserOrReadOnly
from .serializers import (
    TagSerializer,
    AvaterSerializer,
    CategorySerializer,
    ArticleDetailSerializer,
    ArticleSerializer,
    CategoryDetailSerializer
)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_class = ArticleFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        return ArticleDetailSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        return CategoryDetailSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    pagination_class = None


class AvatarViewSet(viewsets.ModelViewSet):
    queryset = Avater.objects.all()
    serializer_class = AvaterSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    pagination_class = None
