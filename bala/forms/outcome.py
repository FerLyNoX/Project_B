from django.forms import  ModelForm, DateTimeField
from .widgets import DatePickerInput, DateTimePickerInput
from bala.models import Outcomes

__all__ = ('OutcomeForm', )


class OutcomeForm(ModelForm):
    class Meta:
        model = Outcomes
        fields = ['date', 'sum', 'project', 'worker', ]
        widgets={
            'date': DatePickerInput(),
        }



