from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from bala.models import Project, ProjectMembers, Incomes, Outcomes
from .urls import get_urls
from django.urls import reverse_lazy
from django_filters import FilterSet


def update_context(context, **kwargs):
    context.update({
        'urls': get_urls(),
        'active_menu': 'projects',
        'title': 'Проекты',
    **kwargs,
    })
    return context


class ProjectFilter(FilterSet):

    class Meta:
        model = Project
        fields = ('name', 'customer', 'area', 'cost',)


class ProjectListView(LoginRequiredMixin,ListView):
    model = Project
    paginate_by = 10
    context_object_name = 'projects'
    template_name = 'project_list.html'

    def get_queryset(self):
        fff = ProjectFilter(self.request.GET, queryset=Project.objects.order_by('id'))
        return fff.qs

    def get_context_data(self, *args, **kwargs):
        fff = ProjectFilter(self.request.GET, queryset=Project.objects.order_by('id'))
        return update_context(
            super().get_context_data(*args, **kwargs),
            filter=fff,
        )


class ProjectEditView(LoginRequiredMixin,UpdateView):
    model = Project
    template_name = 'project_item.html'
    fields = ('name', 'customer', 'area', 'cost', 'description',)
    success_url = reverse_lazy('projects')

    def get_context_data(self, *args, **kwargs):
        instance = self.get_object()
        # планируемые выплаты по проекту
        outcomes_plan = ProjectMembers.objects.filter(project=instance).aggregate(sum=Sum('sum'))
        # фактические посутпления
        incomes_fact = Incomes.objects.filter(project=instance).aggregate(sum=Sum('sum'))
        # фактические выплаты
        outcomes_fact = Outcomes.objects.filter(project=instance).order_by('date').aggregate(sum=Sum('sum'))
        return update_context(
            super().get_context_data(**kwargs),
            outcomes_plan=outcomes_plan,
            incomes_fact=incomes_fact,
            outcomes_fact=outcomes_fact,
        )


class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    template_name = 'item.html'
    fields = ('name', 'customer', 'area', 'cost', 'description',)
    success_url = reverse_lazy('projects')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    model = Project
    template_name = 'item_delete.html'
    success_url = reverse_lazy('projects')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))
