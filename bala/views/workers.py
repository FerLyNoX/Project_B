from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.db.models import Sum
from bala.models import Worker, Outcomes, ProjectMembers
from .urls import get_urls
from django.urls import reverse_lazy

def update_context(context, **kwargs):
    context.update({
        'urls': get_urls(),
        'active_menu': 'workers',
        **kwargs,
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
    template_name = 'worker_item.html'
    fields = ('name', 'price', 'job', 'description',)
    success_url = reverse_lazy('workers')


    def get_context_data(self, *args, **kwargs):
        instance = self.get_object()
        # планируемые выплаты по работнику
        plan = ProjectMembers.objects.filter(worker=instance).aggregate(sum=Sum('sum'))
        # фактические выплаты работнику
        fact = Outcomes.objects.filter(worker=instance).aggregate(sum=Sum('sum'))
        return update_context(super().get_context_data(**kwargs), plan=plan, fact=fact)


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
