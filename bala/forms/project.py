from django.forms import ModelForm, DateTimeField
from .widgets import DatePickerInput, DateTimePickerInput
from bala.models import Project

__all__ = ('ProjectForm',)


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'customer', 'area', 'cost', ]
        widgets = {
            'date': DatePickerInput(),
        }
