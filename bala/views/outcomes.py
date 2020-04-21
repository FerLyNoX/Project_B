from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from bala.models import Outcomes
from .urls import get_urls
from django.urls import reverse_lazy


def update_context(context):
    context.update({
        'urls': get_urls(),
        'active_menu': 'outcomes',
    })
    return context


class OutcomesListView(ListView):
    model = Outcomes
    paginate_by = 10
    context_object_name = 'outcomes'
    template_name = 'outcomes_list.html'

    def get_context_data(self, *args, **kwargs):
        return update_context(
            super().get_context_data(*args, **kwargs)
        )


class OutcomesEditView(UpdateView):
    model = Outcomes
    template_name = 'item.html'
    fields = ('date', 'project', 'worker', 'sum',)
    success_url = reverse_lazy('outcomes')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class OutcomesCreateView(CreateView):
    model = Outcomes
    template_name = 'item.html'
    fields = ('date', 'project', 'worker', 'sum',)
    success_url = reverse_lazy('outcomes')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class OutcomesDeleteView(DeleteView):
    model = Outcomes
    template_name = 'item_delete.html'
    success_url = reverse_lazy('outcomes')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))
