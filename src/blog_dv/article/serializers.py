from rest_framework import serializers
from common.serializers import CommentSerializer
from .models import Article, Avater, Category, Tag
from user_info.serializers import UserDescSerializer


class TagSerializer(serializers.HyperlinkedModelSerializer):

    @staticmethod
    def check_tag_obj_exist(validated_data):
        text = validated_data.get('text')
        if Tag.objects.filter(text=text).exists():
            raise serializers.ValidationError(f'Tag with text {text} is exist')

    def create(self, validated_data):
        self.check_tag_obj_exist(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.check_tag_obj_exist(validated_data)
        return super().update(instance, validated_data)

    class Meta:
        model = Tag
        fields = "__all__"


class AvaterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='avater-detail')

    class Meta:
        model = Avater
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = "__all__"


class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author = UserDescSerializer(read_only=True)
    # category
    category = CategorySerializer(read_only=True)
    tags = serializers.SlugRelatedField(queryset=Tag.objects.all(),
                                        many=True,
                                        required=False,
                                        slug_field="text")

    def to_internal_value(self, data):
        tags_data = data.get("tags")
        if isinstance(tags_data, list):
            for text in tags_data:
                if not Tag.objects.filter(text=text).exists():
                    Tag.objects.create(text=text)
        return super().to_internal_value(data)

    category_id = serializers.IntegerField(write_only=True,
                                           allow_null=True,
                                           required=False)

    @staticmethod
    def validate_category_id(value):
        if not Category.objects.filter(
                id=value).exists() and value is not None:
            raise serializers.ValidationError(
                f"Category with id {value} not exists")
        return value

    avator = AvaterSerializer(read_only=True)
    avator_id = serializers.IntegerField(write_only=True,
                                         allow_null=True,
                                         required=False)

    @staticmethod
    def validate_avator_id(value):
        if not Avater.objects.filter(id=value).exists and value is not None:
            raise serializers.ValidationError(
                f"Avator with id {value} not exists")
        return value


class ArticleSerializer(ArticleBaseSerializer):

    class Meta:
        model = Article
        fields = "__all__"
        extra_kwargs = {"created": {"write_only": True}}


class ArticleDetailSerializer(ArticleBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    comment = CommentSerializer(many=True, read_only=True)
    body_html = serializers.SerializerMethodField()
    toc_html = serializers.SerializerMethodField()

    @staticmethod
    def get_body_html(obj):
        return obj.get_md()[0]

    @staticmethod
    def get_toc_html(obj):
        return obj.get_md()[1]

    class Meta:
        model = Article
        fields = "__all__"


class ArticleCategoryDetailSerializer(serializers.ModelSerializer):
    '''
    aaa
    '''
    url = serializers.HyperlinkedIdentityField(view_name="article-detail")

    class Meta:
        model = Article
        fields = "__all__"


class CategoryDetailSerializer(serializers.ModelSerializer):
    '''
    aaa
    '''
    articles = ArticleCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"
