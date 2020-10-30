from django.urls import path
from django.conf.urls import url
from .views import HomeView, GetHelpView, GetHelpSuccess, ApplicationUpdateView, \
    ApplicationDeleteView, NotesUpdateView
from django.shortcuts import HttpResponse
from django.conf import settings
from django.views.static import serve
from django.core.exceptions import ObjectDoesNotExist
from . import views


def protected_serve(request, path, file_root=None):
    try:
        if request.user.is_superuser:
            return serve(request, path, file_root)
        else:
            usersurl = request.user.cv.url
            file_requested = '/uploads/' + path
            print(request.user.is_superuser)
            if(usersurl == file_requested):
                return serve(request, path, file_root)
            else:
                return HttpResponse("You do not have permission")
    except:
        return HttpResponse("You do not have permission")


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('original/', views.original, name='original'),
    path('table/', views.TableView, name='table'),
    path('table/<int:pk>', ApplicationUpdateView.as_view(), name='application_update'),
    path('get-help/', GetHelpView.as_view(), name='get_help'),
    path('get-help/success', GetHelpSuccess.as_view(), name='get_help_success'),
    path('table/<int:pk>/delete', ApplicationDeleteView.as_view(), name='application_delete'),
    path('table/<int:pk>/notes', NotesUpdateView.as_view(), name='notes'),
    url(r'^{}(?P<path>.*)$'.format(settings.MEDIA_URL[1:]), protected_serve, {'file_root': settings.MEDIA_ROOT}),
]# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)