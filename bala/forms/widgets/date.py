from django.forms import DateTimeInput, DateInput

__all__ = ('DatePickerInput', 'DateTimePickerInput')


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