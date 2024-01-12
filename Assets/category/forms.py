# forms.py

from django import forms
from .models import AssetProperty


class AssetPropertyForm(forms.ModelForm):
    class Meta:
        model = AssetProperty
        fields = ["property", "property_value"]
