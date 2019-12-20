from django import forms

class VoterForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'input',
            'placeholder': 'email'
        })
    )