import django_filters
from .models import Employee

class EmployeeFilter(django_filters.FilterSet):

    # Filter by designation (case-insensitive). Here iexact handle case sensitivity.
    designation = django_filters.CharFilter(
        field_name='designation',
        lookup_expr='iexact'
    )

    class Meta:
        # Apply filters on the Employee model.
        model = Employee

        # Fields allowed for filtering.
        fields = ['designation']