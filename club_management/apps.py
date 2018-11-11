from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ClubsConfig(AppConfig):
    name = 'club_management'
    verbose_name = _('Club Management')
