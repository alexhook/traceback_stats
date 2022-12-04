from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StatsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'traceback_stats.stats'
    verbose_name = _('Traceback statistics')
