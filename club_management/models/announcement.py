import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _

class Announcement(models.Model):
    code = models.CharField(max_length=20, unique=True, blank=True,
        validators=[RegexValidator('^[a-z0-9]+$', _('Club code name must be made of characters and/or numbers.'))])
    title = models.CharField(max_length=100,
        verbose_name=_('announcement title'))
    is_public = models.BooleanField(db_index=True, default=False,
        verbose_name=_('publicly visible'))
    date_posted = models.DateTimeField(verbose_name=_('published on'))
    content = models.TextField(blank=True,
        verbose_name=_('announcement content'))

    def __str__(self):
        return self.title

    class Meta:
        permissions = (
            ('public_announcement', 'Change is_public field for announcements'),
        )
        verbose_name=_('announcement')
        verbose_name_plural=_('announcements')
