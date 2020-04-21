from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from bala.models import ProjectMembers
from .urls import get_urls
from django.urls import reverse_lazy


def update_context(context):
    context.update({
        'urls': get_urls(),
        'active_menu': 'projects',
    })
    return context


class ProjectMembersListView(ListView):
    model = ProjectMembers
    paginate_by = 10
    context_object_name = 'project-members'
    template_name = 'members_list.html'

    def get_context_data(self, *args, **kwargs):
        return update_context(
            super().get_context_data(*args, **kwargs)
        )


class ProjectMembersEditView(UpdateView):
    model = ProjectMembers
    template_name = 'item.html'
    fields = ('project', 'worker', 'amount', 'sum',)
    success_url = reverse_lazy('project-members')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class ProjectMembersCreateView(CreateView):
    model = ProjectMembers
    template_name = 'item.html'
    fields = ('project', 'worker', 'amount', 'sum',)
    success_url = reverse_lazy('projects')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class ProjectMembersDeleteView(DeleteView):
    model = ProjectMembers
    template_name = 'item_delete.html'
    success_url = reverse_lazy('projects')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))
