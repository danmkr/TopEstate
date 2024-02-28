import django_filters
from createPost.models import Anunt

class AnuntFilter(django_filters.FilterSet):
    pret = django_filters.RangeFilter()
    class Meta:
        model = Anunt
        fields = {
            'localizare': ['icontains'],
            'tip_proprietate': ['exact'],
            'tip_vanzare': ['exact'],
            'tip_anunt': ['exact']}