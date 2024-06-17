from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from markdown import Markdown


class Category(models.Model):
    '''
    :param title: 标签名
    :param created: 创建时间
    文章分类
    '''
    title = models.CharField(max_length=100)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_category'
        ordering = ['-created']


class Tag(models.Model):
    """
    标签
    :param  text: 标签名
    """
    text = models.CharField(verbose_name='标签', max_length=100)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'blog_tag'
        ordering = ['-id']


class Avater(models.Model):
    """
    标题图片
    """
    content = models.ImageField(upload_to='avater/%Y%m%d/', blank=True)

    class Meta:
        db_table = "blog_Avater"


class Article(models.Model):
    """
    文章
    """

    title = models.CharField(verbose_name="标题", max_length=100)
    body = models.TextField(verbose_name="正文")
    created = models.DateTimeField(verbose_name="创建时间", default=timezone.now)
    updated = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    tags = models.ManyToManyField(Tag, verbose_name="标签", blank=True, related_name="articles")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="分类",
                                 related_name="category")
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="作者",
                               related_name="user")

    avatar = models.ForeignKey(Avater, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="标题",
                               related_name="avatar")

    def __str__(self):
        return self.title

    def get_md(self):
        md = Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        md_body = md.convert(self.body)
        return md_body, md.toc

    class Meta:
        db_table = 'blog_article'
        ordering = ['-created']
