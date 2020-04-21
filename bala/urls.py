from django.urls import path

from bala.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('jobs/', JobListView.as_view(), name='jobs'),
    path('jobs/<int:pk>/', JobEditView.as_view(), name='job-item'),
    path('jobs/add/', JobCreateView.as_view(), name='job-create'),
    path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
    path('workers/', WorkerListView.as_view(), name='workers'),
    path('workers/<int:pk>/', WorkerEditView.as_view(), name='worker-item'),
    path('workers/add/', WorkerCreateView.as_view(), name='worker-create'),
    path('workers/<int:pk>/delete/', WorkerDeleteView.as_view(), name='worker-delete'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectEditView.as_view(), name='project-item'),
    path('projects/add/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('incomes/', IncomesListView.as_view(), name='incomes'),
    path('incomes/<int:pk>/', IncomesEditView.as_view(), name='incomes-item'),
    path('incomes/add/', IncomesCreateView.as_view(), name='incomes-create'),
    path('incomes/<int:pk>/delete/', IncomesDeleteView.as_view(), name='incomes-delete'),
    path('outcomes/', OutcomesListView.as_view(), name='outcomes'),
    path('outcomes/<int:pk>/', OutcomesEditView.as_view(), name='outcomes-item'),
    path('outcomes/add/', OutcomesCreateView.as_view(), name='outcomes-create'),
    path('outcomes/<int:pk>/delete/', OutcomesDeleteView.as_view(), name='outcomes-delete'),
    path('members/', ProjectMembersListView.as_view(), name='members'),
    path('members/<int:pk>/', ProjectMembersEditView.as_view(), name='members-item'),
    path('members/add/', ProjectMembersCreateView.as_view(), name='members-create'),
    path('members/<int:pk>/delete/', ProjectMembersDeleteView.as_view(), name='members-delete'),
 ]