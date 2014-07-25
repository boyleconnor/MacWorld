from Couches.models import CouchesProfile, Couch
from django.forms import ModelForm


class CouchesProfileForm(ModelForm):
    """
    Form for creating or editing "Couches" profile
    """
    class Meta:
        model = CouchesProfile
        fields = ['description', 'contact_information', 'graduation_year']


class CouchForm(ModelForm):
    """
    Form for creating or editing Couches
    """
    class Meta:
        model = Couch
        fields = ['owner', 'lon', 'lat']