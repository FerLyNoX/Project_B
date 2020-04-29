from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.forms import ModelForm, DateField, SelectDateWidget
from django.urls import reverse_lazy
from django_filters import FilterSet, DateRangeFilter, DateFromToRangeFilter
from django_filters.widgets import DateRangeWidget
from .urls import get_urls
from bala.models import Incomes
from bala.forms import IncomeForm
from bala.forms.widgets import DateRangePickerInput
from django.contrib.auth.mixins import LoginRequiredMixin

def update_context(context, **kwargs):
    context.update({
        'urls': get_urls(),
        'active_menu': 'incomes',
        'title': 'Поступления',
        **kwargs,
    })
    return context



class IncomesFilter(FilterSet):
    period = DateFromToRangeFilter(field_name='date', label='За период',widget=DateRangePickerInput(attrs={'placeholder': 'YYYY/MM/DD'}))

    class Meta:
        model = Incomes
        fields = ('project', 'sum', 'period')


class IncomesListView(ListView):
    model = Incomes
    paginate_by = 10
    context_object_name = 'incomes'
    template_name = 'incomes_list.html'

    def get_queryset(self):
        filter = IncomesFilter(self.request.GET, queryset=Incomes.objects.all())
        return filter.qs

    def get_context_data(self, *args, **kwargs):
        filter = IncomesFilter(self.request.GET, queryset=Incomes.objects.all())
        return update_context(
            super().get_context_data(*args, **kwargs),
            filter=filter,
        )


class IncomesEditView(UpdateView):
    model = Incomes
    template_name = 'item.html'
    success_url = reverse_lazy('incomes')
    form_class = IncomeForm

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
