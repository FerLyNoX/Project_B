from django.views.generic.base import TemplateView
from .urls import get_urls
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'site_author': 'Данчик',
            'urls': get_urls(),
            'active_menu': 'home',
        }

