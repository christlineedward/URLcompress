from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from .models import URLMapping
from .forms import URLMappingForm

# Create your views here.

# Define a list view for all URLMapping objects
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

# Define a view for creating a new URLMapping object
class URLMappingCreateView(CreateView):
    '''
    A View that creates a new URLMapping object.
    Inherits from Django's CreateView class
    '''

    # Specify the model to use for the view
    model = URLMapping

    # Specify the form class to use for the view
    form_class = URLMappingForm

    # Specify the template to render for the view
    template_name = 'create_url_mapping.html'

    def form_valid(self, form):
        # Called when the submitted form is valid
        # Save the form and redirect to the URLMapping list view
        self.object = form.save()
        return redirect('/urlmappings/')
