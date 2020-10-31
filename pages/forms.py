from django import forms

from accounts.helper import file_size

class NewApplication(forms.Form):

    PRIORITY_CHOICES = [ ("Low", "Low"), ("Medium", "Medium"), ('High', 'High'),]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES)
    industry = forms.CharField(max_length=150)
    company = forms.CharField(max_length=150)
    open_date = forms.DateField(initial="DD/MM/YYYY", required=False, widget=forms.TextInput(
        attrs={
            'class': 'datepicker'
        }))
    close_date = forms.DateField(initial="DD/MM/YYYY", required=False, widget=forms.TextInput(
        attrs={
            'class': 'datepicker'
        }))
    link = forms.URLField(initial="")

class GetHelpForm(forms.Form):

    SESSION_TYPE_OPTIONS = [('1','30 Min free intro to expert'),('2', '60 Minute Session')]
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
    problem = forms.CharField( widget=forms.Textarea(attrs={'rows': 3, 'cols': 5}))


