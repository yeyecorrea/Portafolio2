from django.views.generic import ListView
from .models import Home
from applications.work.models import Project, Category
from applications.service.models import Service
from applications.about.models import About
# Create your views here.

class HomeListView(ListView):
    model = Home
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['home'] = Home.objects.all()
            context['category'] = Category.objects.all()
            context['workhome'] = Project.objects.order_by('-created')[:6]
            context['servicehome'] = Service.objects.all()
            context['about'] = About.objects.all()
            return context