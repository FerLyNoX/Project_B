from django.contrib import admin
from bala.models import Project, Job, Worker, Incomes, Outcomes, ProjectMembers

admin.site.register(Project)
admin.site.register(Job)
admin.site.register(Worker)
admin.site.register(Outcomes)
admin.site.register(Incomes)
admin.site.register(ProjectMembers)
