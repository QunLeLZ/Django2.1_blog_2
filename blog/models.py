from django.db import models
from django.utils.timezone import now
from markdownx.models import MarkdownxField

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='类别名称',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '类别名称'
        verbose_name_plural = '类别列表'

class Tag(models.Model):
    name = models.CharField(verbose_name='标签',max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = '标签'
        verbose_name_plural = '标签列表'

class Article(models.Model):
    title = models.CharField(verbose_name='标题',max_length=70)
    body = MarkdownxField(verbose_name='正文',blank=True,null=True)
    abstract = models.TextField(verbose_name='简介',blank=True,null=True)
    create_time = models.DateTimeField(verbose_name='创建时间',default=now)
    views = models.PositiveIntegerField(verbose_name='浏览量',default=0)
    last_mod_time = models.DateTimeField(verbose_name='修改时间',default=now)
    tags = models.ManyToManyField(Tag,verbose_name='标签集合',blank=True)
    category = models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE,blank=False,null=False)

    def __str__(self):
        return self.title

    def viewed(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-create_time']
        verbose_name = '文章'
        verbose_name_plural = '文章列表'

class Gbook(models.Model):
    name = models.CharField(verbose_name='名字',max_length=100)
    email = models.EmailField(verbose_name='邮箱',max_length=255)
    text = models.TextField(verbose_name='内容')
    create_time = models.DateTimeField(verbose_name='评论时间',auto_now_add=True)

    def __str__(self):
        return self.text[:20]

    class Meta:
        ordering = ['-create_time']
        verbose_name = '评论'
        verbose_name_plural = '评论列表'
        get_latest_by = 'create_time'
