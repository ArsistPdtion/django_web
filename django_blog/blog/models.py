from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

#文章标签信息
class Tag(models.Model):
    name = models.CharField(max_length=20,verbose_name='标签')

    def __str__(self):
        return self.name

# 文章分类信息
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类')

    def __str__(self):
        return self.name


#文章信息
class Article(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    desc = models.CharField(max_length=255,verbose_name='简介')
    content = models.TextField(verbose_name='正文')
    pub_date = models.DateTimeField(verbose_name='发布时间')
    mod_date = models.DateTimeField(verbose_name='修改时间')
    author = models.ForeignKey(User,verbose_name='作者')
    tags = models.ManyToManyField(Tag,verbose_name='标签',blank=True)
    category = models.ForeignKey(Category,verbose_name='分类')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'id':self.id})








