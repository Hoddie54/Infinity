from django.views.generic import TemplateView, ListView, FormView
from .models import Article, Section
from .forms import ProfileForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail

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

class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        data = form.cleaned_data
        print(self.request.user.first_name)
        send_mail(
            'Free session request',
            ('Hi admin! ' + "A user called " + self.request.user.first_name + " "
             + self.request.user.last_name + " has asked for some help. More information is attached." + data.__str__()
             + "\n \n User: " + self.request.user.__str__()
             ),
            'office@infinitycareers.co.uk',
            ('hoddie54@gmail.com', 'azharharis18@gmail.com'),
        )
        return super(ProfileView, self).form_valid(form)






