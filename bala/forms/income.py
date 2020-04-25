from django.forms import  ModelForm, DateTimeField
from .widgets import DatePickerInput, DateTimePickerInput
from bala.models import Incomes

__all__ = ('IncomeForm', )

class IncomeForm(ModelForm):
    date2 = DateTimeField(widget=DateTimePickerInput())

    class Meta:
        model = Incomes
        fields = ['date', 'sum', 'project', 'date2']
        widgets={
            'date': DatePickerInput(),
        }



