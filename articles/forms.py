from django import forms

class ProfileForm(forms.Form):

    SESSION_TYPE_CHOICES = [('1', '30 Minute Free Session'), ('2', '60 Minute Paid Session')]

    session_type = forms.ChoiceField(label="", choices=SESSION_TYPE_CHOICES, widget=forms.RadioSelect)
    message = forms.CharField(label="", initial="Hi Azhar, I'm looking for some help on my applications. Are you available for a free meeting with me?", max_length=1500, widget=forms.Textarea(attrs={
        'rows': 3
    }))
