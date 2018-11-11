import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

class Club(models.Model):
    code = models.CharField(max_length=20, unique=True, blank=True,
        validators=[RegexValidator('^[a-z0-9]+$', _('Problem code must be made of characters and/or numbers.'))])
    name = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField('date published')
    executives = models.CharField(max_length=400, blank=True,
        help_text=_('The executives of the club.'))
    description = models.TextField(blank=True, help_text=_('A description of the club.'))

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days>=1)

    class Meta:
        app_label = 'club_management'
        db_table = 'club'
