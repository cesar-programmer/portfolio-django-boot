from django.views.generic import TemplateView
from .models import Project

class ProjectsView(TemplateView):
    template_name = 'projectsShow/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context