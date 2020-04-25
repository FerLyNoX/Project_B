from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from bala.models import Outcomes
from .urls import get_urls
from django.urls import reverse_lazy
from django_filters import FilterSet, DateRangeFilter, DateFromToRangeFilter
from bala.forms.widgets import DateRangePickerInput
from bala.forms import OutcomeForm


def update_context(context, **kwargs):
    context.update({
        'urls': get_urls(),
        'active_menu': 'outcomes',
        **kwargs,
    })
    return context


class OutcomesFilter(FilterSet):
    period = DateFromToRangeFilter(field_name='date', label='За период',
                                   widget=DateRangePickerInput(attrs={'placeholder': 'YYYY/MM/DD'}))

    class Meta:
        model = Outcomes
        fields = ('project', 'sum', 'period', 'worker',)


class OutcomesListView(ListView):
    model = Outcomes
    paginate_by = 10
    context_object_name = 'outcomes'
    template_name = 'outcomes_list.html'

    def get_queryset(self):
        fff = OutcomesFilter(self.request.GET, queryset=Outcomes.objects.all())
        return fff.qs

    def get_context_data(self, *args, **kwargs):
        fff = OutcomesFilter(self.request.GET, queryset=Outcomes.objects.all())
        return update_context(
            super().get_context_data(*args, **kwargs),
            filter=fff,
        )


class OutcomesEditView(UpdateView):
    model = Outcomes
    template_name = 'item.html'
    form_class = OutcomeForm
    success_url = reverse_lazy('outcomes')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class OutcomesCreateView(CreateView):
    model = Outcomes
    template_name = 'item.html'
    form_class = OutcomeForm
    success_url = reverse_lazy('outcomes')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class OutcomesDeleteView(DeleteView):
    model = Outcomes
    template_name = 'item_delete.html'
    success_url = reverse_lazy('outcomes')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))
