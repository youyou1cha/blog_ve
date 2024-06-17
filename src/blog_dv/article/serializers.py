from rest_framework import serializers

from .models import Article, Avater, Category, Tag


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
