from django import forms
from django.forms import TextInput, Select, NumberInput, Textarea

from createPost.models import Anunt


class AnuntForm(forms.ModelForm):
    class Meta:
        model = Anunt
        fields = '__all__'

        widgets = {
        'tip_proprietate': Select(attrs={'class': 'form-control'}),
        'tip_vanzare': Select(attrs={'class': 'form-control'}),
        'titul_anunt': TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdu un titlu'}),
        'suprafata_utila': NumberInput(attrs={'class':'form-control', 'placeholder': 'Introdu suprafata utila'}),
        'pret': NumberInput(attrs={'class':'form-control', 'placeholder': 'Introdu pretul'}),
        'localizare': TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdu adresa'}),
        'descriere': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3})
        }