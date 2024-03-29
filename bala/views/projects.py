from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum,Subquery, OuterRef, F, Case, When, Count
from bala.models import Project, ProjectMembers, Incomes, Outcomes
from .urls import get_urls
from django.urls import reverse_lazy, reverse
from django_filters import FilterSet
from django.shortcuts import get_object_or_404


def update_context(context, **kwargs):
    context.update({
        'urls': get_urls(),
        'active_menu': 'projects',
        'title': 'Проекты',
        **kwargs,
    })
    return context

class ProjectToggleClose(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projects')

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Project, pk=kwargs['pk'])
        obj.closed = not obj.closed
        obj.save()
        return super().get(request, *args, **kwargs)


class ProjectFilter(FilterSet):

    class Meta:
        model = Project
        fields = ('name', 'customer', 'area', 'cost', 'closed')
        initial = {'closed': False}



class ProjectListView(LoginRequiredMixin,ListView):
    model = Project
    paginate_by = 10
    context_object_name = 'projects'
    template_name = 'project_list.html'

    @property
    def qs(self):
        sub1 = Incomes.objects.filter(project=OuterRef('pk')).order_by('date')
        sub2 = Incomes.objects.filter(project=OuterRef('pk')).order_by('-date')
        qs = Project.objects.all().annotate(
            inc_count = Count('incomes__id')
        ).annotate(
            pay_sum1 = Subquery(sub1.values('sum')[:1]),
            pay_date1= Subquery(sub1.values('date')[:1]),
            balance_sum=F('cost')-Sum('incomes__sum'),
            pay_sum2 = Case(
                When(inc_count__gt = 1, then =Subquery(sub2.values('sum')[:1])),
                default=None
            ),
            pay_date2=Case(
                When(inc_count__gt=1, then=Subquery(sub2.values('date')[:1])),
                default=None
            ),
        )
        return qs

    def get_queryset(self):
        fff = ProjectFilter(self.request.GET, queryset=self.qs)
        return fff.qs

    def get_context_data(self, *args, **kwargs):
        fff = ProjectFilter(self.request.GET, queryset=self.qs)
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
