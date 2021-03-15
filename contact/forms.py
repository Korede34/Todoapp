from django.forms import  ModelForm
from .models import Contact


class ContactDetails(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'