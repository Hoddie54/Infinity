from django.views.generic import TemplateView, ListView
from .models import Article, Section
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleView(TemplateView):
    template_name = 'articles/article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        sections = Section.objects.all().filter(article_id=self.kwargs.get('pk'))
        context['sections'] = sections
        context['article'] = Article.objects.get(id=self.kwargs.get('pk'))
        return context

class DashboardView(LoginRequiredMixin, ListView):
    template_name = 'articles/dashboard.html'
    model = Article
    context_object_name = 'articles'

    def get_queryset(self):
        result = super(DashboardView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Article.objects.filter(Q(title__contains=query) | Q(firm__name__contains=query))
            postresult = postresult.filter(firm__image__isnull=False)
            result = postresult
        else:
            result = Article.objects.filter(firm__image__isnull=False)
        return result

