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
