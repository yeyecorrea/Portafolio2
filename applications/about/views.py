from django.views.generic import ListView
from .models import About
# Create your views here.

class AboutListView(ListView):
    model = About
    template_name = 'about/about.html'
    context_object_name = 'about'
