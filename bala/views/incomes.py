from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from bala.models import Incomes
from .urls import get_urls
from django.urls import reverse_lazy


def update_context(context):
    context.update({
        'urls': get_urls(),
        'active_menu': 'incomes',
    })
    return context


class IncomesListView(ListView):
    model = Incomes
    paginate_by = 10
    context_object_name = 'incomes'
    template_name = 'incomes_list.html'

    def get_context_data(self, *args, **kwargs):
        return update_context(
            super().get_context_data(*args, **kwargs)
        )


class IncomesEditView(UpdateView):
    model = Incomes
    template_name = 'item.html'
    fields = ('date', 'project', 'sum',)
    success_url = reverse_lazy('incomes')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class IncomesCreateView(CreateView):
    model = Incomes
    template_name = 'item.html'
    fields = ('date', 'project', 'sum',)
    success_url = reverse_lazy('incomes')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class IncomesDeleteView(DeleteView):
    model = Incomes
    template_name = 'item_delete.html'
    success_url = reverse_lazy('incomes')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))
