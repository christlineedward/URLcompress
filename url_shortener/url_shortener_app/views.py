from django.shortcuts import render
from django.views.generic import ListView
from .models import URLMapping

# Create your views here.

# Define a viewset for URLMapping Model
class URLMappingListView(ListView):
   '''
   A View that displays a list of URLMappings.
   Inherits from Django's ListView class'''

   # Specify the model to use for the view
   model = URLMapping

   # Specify the template to render for the view
   template_name = 'url_mapping_list.html'

   # Specify the context variable name to use in the template
   context_object_name = 'urlmappings'
