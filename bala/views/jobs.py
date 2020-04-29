from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from bala.models import Job
from .urls import get_urls
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def update_context(context):
    context.update({
        'urls': get_urls(),
        'active_menu': 'jobs',
        'title': 'Проекты',
    })
    return context


class JobListView(LoginRequiredMixin,ListView):
    model = Job
    paginate_by = 10
    context_object_name = 'jobs'
    template_name = 'job_list.html'

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class JobEditView(LoginRequiredMixin,UpdateView):
    model = Job
    template_name = 'item.html'
    fields = ('name', 'description')
    success_url = reverse_lazy('jobs')

    def get_context_data(self, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class JobCreateView(LoginRequiredMixin,CreateView):
    model = Job
    template_name = 'item.html'
    fields = ('name', 'description')
    success_url = reverse_lazy('jobs')

    def get_context_data(self, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class JobDeleteView(LoginRequiredMixin,DeleteView):
    model = Job
    template_name = 'item_delete.html'
    success_url = reverse_lazy('jobs')

    def get_context_data(self, **kwargs):
        return update_context(super().get_context_data(**kwargs))
