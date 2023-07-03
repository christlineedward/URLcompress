from django import forms
from .models import URLMapping

# Note: we get form validation on `long_url` for free since it'll throw an error if we try to write it to the database. 
class URLMappingForm(forms.ModelForm):
    class Meta:
        model = URLMapping
        fields = ['short_code', 'long_url']
