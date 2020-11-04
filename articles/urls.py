from django.urls import path
from .views import ArticleView, DashboardView, ProfileView
from django.views.generic import TemplateView

urlpatterns = [
    path('article/<int:pk>/', ArticleView.as_view(), name='article'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('article/mckinsey/', TemplateView.as_view(template_name='articles/mckinsey.html'), name='mckinsey'),
    path('article/mckinsey/1/', TemplateView.as_view(template_name='articles/mckinsey_article.html'), name='mckinsey_article'),
    path('profile/azhar/', ProfileView.as_view(), name='profile'),
]