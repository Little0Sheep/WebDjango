from django.contrib import admin

from . import models

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display=('headline','ppt_abstract','pub_date','ppt_full_name','state')

admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Reporter)