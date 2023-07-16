from django.views.generic import ListView, DetailView
from .models import Project, Category
# Create your views here.

class WorkListView(ListView):
    model = Project
    template_name = "work/work.html"
    ordering = 'id'
    paginate_by = 2
    context_object_name = 'work'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.all()
        context['category'] = Category.objects.all()
        return context

class WorkDetailView(DetailView):
    model = Project
    template_name = "work/workDetail.html"
    context_object_name = 'project'

