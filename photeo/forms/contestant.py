from django import forms
from photeo.models import Contestant

class ContestantRegistrationForm(forms.ModelForm):
    class Meta:
        model = Contestant
        exclude = ['id']
        fields = ['name', 'email', 'picture', 'title', 'social_account']
        widgets = {
            'name': forms.TextInput(attrs={
                        'class': 'input',
                        'placeholder': 'name'
                    }),
            'email': forms.EmailInput(attrs={
                        'class': 'input',
                        'placeholder': 'email'
                    }),
            # 'picture': forms.ImageField(),
            'title': forms.TextInput(attrs={
                        'class': 'input',
                        'placeholder': 'title'
                    }),
            'social_account': forms.TextInput(attrs={
                                'class': 'input',
                                'placeholder': 'social account'
                            }),
        }