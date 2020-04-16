from django import forms
from bala.models import Job
from crispy_forms.helper import FormHelper


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('name', 'description')
