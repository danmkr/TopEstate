from django import forms
from django.forms import TextInput, Select

from Home.models import Search


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = '__all__'

        widgets = {
        'localitate': TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdu localitatea'}),
        'tip_proprietate': Select(attrs={'class': 'form-select'}),
        'tip_achizitie': Select(attrs={'class': 'form-select'}),
        'categorie': Select(attrs={'class': 'form-select'})
        }
