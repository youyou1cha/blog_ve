from django_filters import rest_framework as filters

from .models import Article


class ArticleFilter(filters.FilterSet):
    """
    list filter
    """
    title = filters.CharFilter(
        field_name='title', lookup_expr='icontains', label='标题'
    )

    class Meta:
        model = Article
        fields = ['title']
