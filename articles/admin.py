from django.contrib import admin
from .models import Firm, Article, Section

class SectionInLine(admin.StackedInline):
    model = Section


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        SectionInLine,
    ]


admin.site.register(Firm)
admin.site.register(Article, ArticleAdmin)

