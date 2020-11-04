from django import forms
from django.forms import ModelForm
from .models import Notes
from articles.models import Firm
from accounts.helper import file_size
from itertools import chain

class NewApplicationForm(forms.Form):

    PRIORITY_CHOICES = [ ("Low", "Low"), ("Medium", "Medium"), ('High', 'High'),]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
    industry = forms.CharField(max_length=150)
    company = forms.ModelChoiceField(queryset=Firm.objects.all(), to_field_name='name')
    open_date = forms.DateField(initial="DD/MM/YYYY", required=False, widget=forms.TextInput(
        attrs={
            'class': 'datepicker'
        }))
    close_date = forms.DateField(initial="DD/MM/YYYY", required=False, widget=forms.TextInput(
        attrs={
            'class': 'datepicker'
        }))
    link = forms.URLField(initial="")

class AutofillForm(forms.Form):
    autofill = forms.BooleanField()

class GetHelpForm(forms.Form):

    SESSION_TYPE_OPTIONS = [('1','30 Minute free introduction to expert'),('2', '60 Minute Paid Session')]
    HELP_AREA_OPTIONS = [('1', "My CV"),('2', "My online tests"), ('3',"Interviews"), ('4', 'Other')]

    session_type = forms.ChoiceField(choices=SESSION_TYPE_OPTIONS, widget=forms.RadioSelect)
    help_area = forms.ChoiceField(choices=HELP_AREA_OPTIONS)
    problem = forms.CharField( widget=forms.Textarea(attrs={'rows': 3, 'cols': 5}))
    cv = forms.FileField(validators=[file_size], required=False)
    additional_files = forms.FileField(validators=[file_size], required=False)

class FreeSessionForm(forms.Form):
    SESSION_TYPE_OPTIONS = [('1','30 Min free intro to expert'),('2', '60 Minute Session')]
    HELP_AREA_OPTIONS = [('1', "My CV"),('2', "My online tests"), ('3',"Interviews"), ('4', 'Other')]

    #session_type = forms.ChoiceField(choices=SESSION_TYPE_OPTIONS, widget=forms.RadioSelect)
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    help_area = forms.ChoiceField(choices=HELP_AREA_OPTIONS)
    problem = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'cols': 5}))

class NotesForm(forms.ModelForm):

    class Meta:
        model = Notes
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NotesForm, self).__init__(*args, **kwargs)
        for i in range(1,6):
            self.fields['notes' + str(i)].widget.attrs['cols'] = 5
            self.fields['notes' + str(i)].widget.attrs['rows'] = 3


