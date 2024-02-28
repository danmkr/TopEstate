import django_filters
from django.forms import TextInput, Select

from createPost.models import Anunt

class AnuntFilter(django_filters.FilterSet):
    pret = django_filters.RangeFilter()
    class Meta:
        model = Anunt
        fields = {
            'localizare': ['icontains'],
            'tip_proprietate': ['exact'],
            'tip_vanzare': ['exact'],
            'tip_anunt': ['exact']
        }
        widgets = {
            'localizare': TextInput(attrs={'class': 'form-control', 'placeholder': 'Introdu localitatea'}),
            'tip_proprietate': Select(attrs={'class': 'form-select'}),
            'tip_vanzare': Select(attrs={'class': 'form-select'}),
            'tip_anunt': Select(attrs={'class': 'form-select'})
        }