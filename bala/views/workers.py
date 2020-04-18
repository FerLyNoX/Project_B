from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from bala.models import Worker
from .urls import get_urls
from django.urls import reverse_lazy

def update_context(context):
    context.update({
        'urls': get_urls(),
        'active_menu': 'workers',
    })
    return context

class WorkerListView(ListView):
    model = Worker
    paginate_by = 10
    context_object_name = 'workers'
    template_name = 'worker_list.html'

    def get_context_data(self, *args, **kwargs):
        return update_context(
            super().get_context_data(*args, **kwargs)
        )


class WorkerEditView(UpdateView):
    model = Worker
    template_name = 'item.html'
    fields = ('name', 'price', 'job', 'description',)
    success_url = reverse_lazy('workers')


    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class WorkerCreateView(CreateView):
    model = Worker
    template_name = 'item.html'
    fields = ('name', 'price', 'job', 'description',)
    success_url = reverse_lazy('workers')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'item_delete.html'
    success_url = reverse_lazy('workers')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))
