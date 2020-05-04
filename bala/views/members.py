from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django_filters import FilterSet, DateRangeFilter, DateFromToRangeFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import OuterRef, Subquery, Sum, Case, When, Count, F, DecimalField
from bala.models import ProjectMembers, Outcomes
from .urls import get_urls


def update_context(context, **kwargs):
    context.update({
        'urls': get_urls(),
        'active_menu': 'project_members',
        'title': 'Участники проектов',
        **kwargs,
    })
    return context


class ProjectMembersFilter(FilterSet):
    class Meta:
        model = ProjectMembers
        fields = ('project', 'worker', 'amount', 'sum',)


class ProjectMembersListView(LoginRequiredMixin,ListView):
    model = ProjectMembers
    paginate_by = 10
    context_object_name = 'project-members'
    template_name = 'members_list.html'

    @property
    def qs(self):
        sub1 = Outcomes.objects.filter(worker=OuterRef('worker_id'), project=OuterRef('project_id')).order_by('date')
        sub2 = Outcomes.objects.filter(worker=OuterRef('worker_id'), project=OuterRef('project_id')).order_by('-date')
        sub1_count = ProjectMembers.objects.filter(worker=OuterRef('worker_id'), worker__payments__project=OuterRef('project_id')).annotate(ccc = Count('worker__payments')).values('ccc')
        sub1_total = ProjectMembers.objects.filter(worker=OuterRef('worker_id'), worker__payments__project=OuterRef('project_id')).annotate(total = Sum('worker__payments__sum')).values('total')
        qs = ProjectMembers.objects.all().annotate(
            payments_count = Subquery(sub1_count)
        ).annotate(
            pay_sum1 = Subquery(sub1.values('sum')[:1]),
            pay_date1= Subquery(sub1.values('date')[:1]),
            balance_sum=F('sum')-Subquery(sub1_total, output_field=DecimalField(max_digits=13, decimal_places=2)),
            pay_sum2 = Case(
                When(payments_count__gt=1, then =Subquery(sub2.values('sum')[:1])),
                default=None
            ),
            pay_date2=Case(
                When(payments_count__gt=1, then=Subquery(sub2.values('date')[:1])),
                default=None
            ),
        )
        return qs

    def get_queryset(self):
        fff = ProjectMembersFilter(self.request.GET, queryset=self.qs)
        return fff.qs

    def get_context_data(self, *args, **kwargs):
        fff = ProjectMembersFilter(self.request.GET, queryset=self.qs)
        return update_context(
            super().get_context_data(*args, **kwargs),
            filter=fff,
        )


class ProjectMembersEditView(LoginRequiredMixin, UpdateView):
    model = ProjectMembers
    template_name = 'item.html'
    fields = ('project', 'worker', 'amount', 'sum',)
    success_url = reverse_lazy('members')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class ProjectMembersCreateView(LoginRequiredMixin, CreateView):
    model = ProjectMembers
    template_name = 'item.html'
    fields = ('project', 'worker', 'amount', 'sum',)
    success_url = reverse_lazy('members')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))


class ProjectMembersDeleteView(LoginRequiredMixin, DeleteView):
    model = ProjectMembers
    template_name = 'item_delete.html'
    success_url = reverse_lazy('members')

    def get_context_data(self, *args, **kwargs):
        return update_context(super().get_context_data(**kwargs))
