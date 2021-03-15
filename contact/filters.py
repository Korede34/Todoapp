import django_filters
from .models import Contact

class Contactfilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ['fullname']