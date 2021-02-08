from django_filters import rest_framework as rf_filters
from .models import Articles

class ArticlesFilters(rf_filters.FilterSet):
    # id = rf_filters.NumberFilter(field_name='id', lookup_exp='lte')

    class Meta:
        model = Articles
        fields = [ 'title', 'body']