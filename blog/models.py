#coding:utf-8
from django.db import models
from django.utils import timezone

# Create your models here.
class Reporter(models.Model):
    full_name=models.CharField(verbose_name='作者',max_length=50)

    def __unicode__(self):
        return self.full_name

class Article(models.Model):
    pub_date=models.DateTimeField(verbose_name='发布日期',default=timezone.now())
    headline=models.CharField(verbose_name='标题',max_length=100)
    abstract=models.CharField(verbose_name='摘要',max_length=300,default=None)
    cover=models.ImageField(verbose_name='封面图片',upload_to='uploadImages')
    content=models.TextField(verbose_name='内容')
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE,verbose_name='作者')

    state_list=(
            (0,'草稿'),
            (1,'已发布'),
                )
    state=models.IntegerField(verbose_name='状态',choices=state_list)

    def property_full_name(self):
        return self.reporter.full_name
    property_full_name.short_description='作者'
    ppt_full_name=property(property_full_name)

    def property_abstract(self):
        return self.abstract[:20]+'......'
    property_abstract.short_description='摘要'
    ppt_abstract=property(property_abstract)

    def __unicode__(self):
        return self.headline