from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from bala.models import Project
from .urls import get_urls
from django.urls import reverse_lazy
from django_filters import FilterSet, DateRangeFilter, DateFromToRangeFilter
from bala.forms.widgets import DateRangePickerInput


def update_context(context, **kwargs):
    context.update({
        'urls': get_urls(),
        'active_menu': 'projects',
        **kwargs,
    })
    return context


class ProjectFilter(FilterSet):

    class Meta:
        model = Project
        fields = ('name', 'customer', 'area', 'cost',)


class ProjectListView(ListView):
    model = Project
    paginate_by = 10
    context_object_name = 'projects'
    template_name = 'project_list.html'

    def get_queryset(self):
        fff = ProjectFilter(self.request.GET, queryset=Project.objects.all())
        return fff.qs

    def get_context_data(self, *args, **kwargs):
        fff = ProjectFilter(self.request.GET, queryset=Project.objects.all())
        return update_context(
            super().get_context_data(*args, **kwargs),
            filter=fff,
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
