from django.views.generic import ListView, DetailView, CreateView, DeleteView
from webapp.models import Projects, Tasks
from django.urls import reverse, reverse_lazy
from webapp.forms import ProjectForm, TaskForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin



class ProjectsView(ListView):
    template_name = 'projects.html'
    model = Projects
    context_object_name = 'projects'
    ordering = ('created_at',)


class ProjectDetailView(DetailView):
    template_name = 'project_detail.html'
    model = Projects
    context_object_name = 'project'

    
class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'project_create.html'
    form_class = ProjectForm
    model = Projects

    def get_success_url(self):
        return reverse('projects')


class ProjectTaskCreateView(LoginRequiredMixin, CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'task_create.html'

    def form_valid(self, form):
        project = get_object_or_404(Projects, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projects')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'article_confirm_delete.html'
    model = Projects
    success_url = reverse_lazy('index')
