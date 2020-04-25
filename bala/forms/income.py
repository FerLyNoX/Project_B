from django.forms import  ModelForm, DateTimeField
from .widgets import DatePickerInput, DateTimePickerInput
from bala.models import Incomes

__all__ = ('IncomeForm', )

class IncomeForm(ModelForm):
    class Meta:
        model = Incomes
        fields = ['date', 'sum', 'project']
        widgets={
            'date': DatePickerInput(),
        }



