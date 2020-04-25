from django.forms import DateTimeInput, DateInput
from django_filters.widgets import DateRangeWidget

__all__ = ('DatePickerInput', 'DateTimePickerInput', 'DateRangePickerInput')


class DatePickerInput(DateInput):
    template_name = 'widgets\datepicker.html'

    def get_context(self, name, value, attrs):
        datepicker_id = f'datepicker_{name}'
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datepicker_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datepicker_id'] = datepicker_id
        return context

class DateRangePickerInput(DateRangeWidget):
    template_name = 'widgets\daterangepicker.html'

    def get_context(self, name, value, attrs):
        datepicker_from_id = f'datepicker_from_{name}'
        datepicker_to_id = f'datepicker_to_{name}'
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datepicker_from_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datepicker_from_id'] = datepicker_from_id
        context['widget']['datepicker_to_id'] = datepicker_to_id
        return context


class DateTimePickerInput(DateTimeInput):
    template_name = 'widgets\datetimepicker.html'

    def get_context(self, name, value, attrs):
        datetimepicker_id =f'datetimepicker_{name}'
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}'.format(id=datetimepicker_id)
        attrs['class'] = 'form-control datetimepicker-input'
        context = super().get_context(name, value, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id
        return context