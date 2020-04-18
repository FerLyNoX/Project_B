from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from bala.models import Project
from .urls import get_urls
from django.urls import reverse_lazy


def update_context(context):
    context.update({
        'urls': get_urls(),
        'active_menu': 'projects',
    })
    return context


class ProjectListView(ListView):
    model = Project
    paginate_by = 10
    context_object_name = 'projects'
    template_name = 'project_list.html'

    def get_context_data(self, *args, **kwargs):
        return update_context(
            super().get_context_data(*args, **kwargs)
        )


class ProjectEditView(UpdateView):
    model = Project
    template_name = 'item.html'
    fields = ('name', 'customer', 'area', 'cost', 'description',)
    success_url = reverse_lazy('projects')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'item.html'
    fields = ('name', 'customer', 'area', 'cost', 'description',)
    success_url = reverse_lazy('projects')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'item_delete.html'
    success_url = reverse_lazy('projects')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))
