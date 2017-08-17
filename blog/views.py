#coding:utf-8
from django.shortcuts import render

from .models import Article
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    column_list={'年度文章':reverse('year_archive',args=(2017,)),'月度文章':reverse('month_archive',args=(2017,'02',))}
    return render(request,'index.html',{'index':'active','column_list':column_list})

def year_archive(request,year):
    a_list=Article.objects.filter(pub_date__year=year)
    context={'year':year,'article_list':a_list}
    return render(request, 'year_archive.html', context)

def month_archive(request,year,month):
    a_list=Article.objects.filter(pub_date__year=year,pub_date__month=month)
    context={'year':year,'month':month,'article_list':a_list}
    return render(request,'month_archive.html',context)

def detail_archive(request,id):
    detail_list=Article.objects.get(id=id)
    context={'article_detail':detail_list}
    return render(request,"detail_archive.html",context)

def article_list(request):
    article_list=Article.objects.filter(state=1)
    context={'blogs':'active','article_list':article_list}
    return render(request,'article_list.html',context)