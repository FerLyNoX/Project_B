from django.urls import reverse

def get_urls():
    return [
        {'caption': 'Главная', 'url': reverse('index'), 'disabled': False, 'name': 'home'},
        {'caption': 'Проекты', 'url': reverse('projects'), 'disabled': True, 'name': 'projects'},
        {'caption': 'Участники проектов', 'url': reverse('members'), 'disabled': True, 'name': 'project-members'},
        {'caption': 'Работники', 'url': reverse('workers'), 'disabled': True, 'name': 'workers'},
        {'caption': 'Работы', 'url': reverse('jobs'), 'disabled': True, 'name': 'jobs'},
        {'caption': 'Поступления', 'url': reverse('incomes'), 'disabled': True, 'name': 'incomes'},
        {'caption': 'Расходы', 'url': reverse('outcomes'), 'disabled': True, 'name': 'outcomes'},
    ]