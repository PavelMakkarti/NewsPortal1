from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from .models import Post
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    dataCreation_after = DateTimeFilter(
        field_name='dataCreation',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
           'title': ['icontains'],
           'postCategory': ['gt'],
           'dataCreation': [
               # 'lt',
               'gt',
],
}