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
 ]