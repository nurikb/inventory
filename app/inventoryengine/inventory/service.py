
from django_filters import rest_framework as filters
from .models import Admission



class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class AdmissionFilter(filters.FilterSet):
    id_type = CharFilterInFilter(field_name='id_type__name', lookup_expr='in')
    date = filters.RangeFilter()

    class Meta:
        model = Admission
        fields = ['id_type', 'date']


