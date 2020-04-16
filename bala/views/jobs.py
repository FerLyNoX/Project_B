from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from bala.models import Job
from .urls import get_urls
from django.urls import reverse_lazy

class JobListView(ListView):
    model = Job
    paginate_by = 2
    context_object_name = 'jobs'
    template_name = 'job_list.html'

    def get_context_data(self, *agrs, **kwargs):
        context = super().get_context_data(*agrs, **kwargs)
        context.update({
            'urls': get_urls(),
            'active_menu': 'jobs',
        })
        return context


class JobEditView(UpdateView):
    model = Job
    template_name = 'job_item.html'
    fields = ('name', 'description')
    success_url = reverse_lazy('jobs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'urls': get_urls(),
            'active_menu': 'jobs',
        })
        return context


class JobCreateView(CreateView):
    model = Job
    template_name = 'job_item.html'
    fields = ('name', 'description')
    success_url = reverse_lazy('jobs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'urls': get_urls(),
            'active_menu': 'jobs',
        })
        return context


class JobDeleteView(DeleteView):
    model = Job
    template_name = 'job_item_delete.html'
    success_url = reverse_lazy('jobs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'urls': get_urls(),
            'active_menu': 'jobs',
        })
        return context
