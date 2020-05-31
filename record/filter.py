from django_filters import DateRangeFilter, DateFilter, FilterSet
from .models import Record


class RecordFilter(FilterSet):
    start_date = DateFilter(field_name='time', lookup_expr='gt')
    end_date = DateFilter(field_name='time', lookup_expr='lt')
    time_range = DateRangeFilter(field_name='time')

    class Meta:
        model = Record
        fields = ('time',)
