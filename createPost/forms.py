from django import forms
from django.forms import TextInput, Select, NumberInput, Textarea

from createPost.models import Anunt, Promovare


class AnuntForm(forms.ModelForm):
    class Meta:
        model = Anunt
        fields = '__all__'

        widgets = {
        'tip_proprietate': Select(attrs={'class': 'form-control'}),
        'tip_vanzare': Select(attrs={'class': 'form-control'}),
        'titul_anunt': TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdu un titlu'}),
        'suprafata_utila': NumberInput(attrs={'class':'form-control', 'placeholder': 'Introdu suprafata utila'}),
        'numar_carte_funciara': TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdu numarul de carte funciara'}),
        'pret': NumberInput(attrs={'class':'form-control', 'placeholder': 'Introdu pretul'}),
        'localizare': TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdu adresa'}),
        'descriere': Textarea(attrs={'class': 'form-control', 'placeholder': 'Introdu descrierea', 'rows': 3}),
        'tip_anunt': Select(attrs={'class': 'form-control'}),
        }

class PromoForm(forms.ModelForm):
    class Meta:
        model = Promovare
        fields = '__all__'

        widgets = {
        'metoda_de_promovare': Select(attrs={'class': 'form-control'})
        }