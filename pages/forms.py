from django import forms
from accounts.helper import file_size

class NewApplication(forms.Form):

    PRIORITY_CHOICES = [ ("Low", "Low"), ("Medium", "Medium"), ('High', 'High'),]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
    industry = forms.CharField(max_length=150)
    company = forms.CharField(max_length=150)
    open_date = forms.DateField(initial="DD/MM/YYYY")
    close_date = forms.DateField(initial="DD/MM/YYYY")
    link = forms.URLField(initial="")

class GetHelpForm(forms.Form):

    SESSION_TYPE_OPTIONS = [('1','30 Min free into to expert'),('2', '60 Minute Session')]
    HELP_AREA_OPTIONS = [('1', "My CV"),('2', "My online tests"), ('3',"Interviews"), ('4', 'Other')]

    session_type = forms.ChoiceField(choices=SESSION_TYPE_OPTIONS, widget=forms.RadioSelect)
    help_area = forms.ChoiceField(choices=HELP_AREA_OPTIONS)
    problem = forms.CharField(max_length=2000)
    cv = forms.FileField(validators=[file_size])

