"""WebDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from blog import views

urlpatterns = [
    url(r'^articles/([0-9]{4})/$',views.year_archive,name='year_archive'),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$',views.month_archive,name='month_archive'),
    url(r'^articles/([0-9]+)/$',views.detail_archive,name='detail_archive'),
    url(r'^blogs/$',views.article_list,name='blogs'),
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
