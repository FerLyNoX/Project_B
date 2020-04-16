from django.urls import path

from bala.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('jobs/', JobListView.as_view(), name='jobs'),
    path('jobs/<int:pk>/', JobEditView.as_view(), name='job-item'),
    path('jobs/add/', JobCreateView.as_view(), name='job-create'),
    path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='job-delete'),
]