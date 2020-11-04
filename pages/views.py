from django.shortcuts import render
from django.views.generic import TemplateView, FormView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Application, Notes, AutoAddApplication
from articles.models import Firm, Article
from .forms import NewApplicationForm, GetHelpForm, FreeSessionForm, NotesForm, AutofillForm
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail


class HomeView(TemplateView):
    template_name = 'home.html'


class GetHelpSuccess(TemplateView):
    template_name = 'get_help_submitted.html'


def original(request):
    return render(request, 'original.html')


def TableView(request):

    form1 = NewApplicationForm()
    form2 = AutofillForm()
    context = {'application_list': Application.objects.all().filter(user=request.user),
               'form1': form1, 'form2': form2}

    if request.method == 'POST':
        #print(request.POST.get('auto_fill') + "hey")
        #print(request.POST)
        if(request.POST.get('auto_fill') == ''):
            for autoapplication in AutoAddApplication.objects.all():
                new_app = Application(
                    priority=autoapplication.priority,
                    user=request.user,
                    open_date=autoapplication.open_date,
                    close_date=autoapplication.close_date,
                    company=autoapplication.company,
                    industry=autoapplication.industry,
                    link=autoapplication.link,
                                      )
                new_app.save()
        else:
            form = NewApplicationForm(request.POST)
            try:
                open = datetime.strptime(request.POST.get('open_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            except:
                open = None
            try:
                close = datetime.strptime(request.POST.get('close_date'), '%d/%m/%Y').strftime('%Y-%m-%d')
            except:
                close = None
            new_app = Application(priority=request.POST.get('priority'), user=request.user,
                                  open_date=open,
                                  close_date=close,
                                  company=request.POST.get('company'),
                                  industry=request.POST.get('industry'),
                                  link=request.POST.get('link'),)
            new_app.save()
            #print(request.POST)
            HttpResponseRedirect('table')

    return render(request, 'table.html', context)



def get_name(request):

    if request.method == 'POST':
        form = NewApplicationForm(request.POST)
        print(request.POST)
        new_app = Application(priority=request.POST.get('priority'), user=request.user)
        new_app.save()
        return HttpResponseRedirect('home')
    else:
        form = NewApplicationForm()

    return render(request, 'name.html', {'form': form})

class GetHelpView(FormView):
    form_class = GetHelpForm
    template_name = 'get_help.html'
    success_url = reverse_lazy('get_help_success')

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        self.request.user.cv = form.cleaned_data.get('cv')
        self.request.user.additional_files = form.cleaned_data.get('additional_files')
        self.request.user.save()
        return super(GetHelpView, self).form_valid(form)

    def send_mail(self, valid_data):
        send_mail(
            'New User Requested Help',
            ('Hi admin! ' + "A user called " + self.request.user.first_name + " "
             + self.request.user.last_name + " has asked for some help. Their problem is " +
             valid_data.get('problem') + ". More information is attached." + valid_data.__str__()
             + "\n \n User: " + self.request.user.__str__()
             ),
            'office@infinitycareers.co.uk',
            ('hoddie54@gmail.com', 'azharharis18@gmail.com'),
        )
        pass

    def get_initial(self):
        initial = super(GetHelpView, self).get_initial()
        initial.update({'cv': self.request.user.cv},)
        return initial


class ApplicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Application
    success_url = reverse_lazy('table')
    template_name = 'application_update.html'

    fields = (
        'priority',
        'industry',
        'company',
        'open_date',
        'close_date',
        'link',
        'stage',
        'link',
    )

    def test_func(self):
        logged_in_user = self.request.user.id
        return logged_in_user == Application.objects.get(pk=self.kwargs.get('pk')).user_id

class ApplicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Application
    template_name = 'application_delete.html'
    success_url = reverse_lazy('table')

    def test_func(self):
        logged_in_user = self.request.user.id
        return logged_in_user == Application.objects.get(pk=self.kwargs.get('pk')).user_id

class NotesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = NotesForm
    model = Notes
    template_name = 'notes.html'
    success_url = reverse_lazy('table')

    def test_func(self):
        logged_in_user = self.request.user

        for application in Application.objects.all().filter(user=logged_in_user):
            if(application.notes.pk == self.kwargs.get('pk')):
                return True
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        #notes_id = self.kwargs.get('pk')
        #app = None
        #for application in Application.objects.all():
         #   if(application.notes_id == notes_id):
          #      app = application
        #print(app)
        #firm = Firm.objects.get(name=app.company)

        #article = Article.objects.filter(firm=firm)[0]
        #context['article'] = article
        return context


class FreeSessionView(FormView):
    form_class = FreeSessionForm
    template_name = 'get_help.html'
    success_url = reverse_lazy('free_session_success')

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super(FreeSessionView, self).form_valid(form)

    def send_mail(self, valid_data):
        'Free 1-to-1 Requested Help',
        ('Hi admin! Here is what is up: ' + valid_data.__str__()

         ),
        'office@infinitycareers.co.uk',
        ('hoddie54@gmail.com', 'azharharis18@gmail.com'),
        pass