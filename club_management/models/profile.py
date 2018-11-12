import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from sortedm2m.fields import SortedManyToManyField

class Club(models.Model):
    code = models.CharField(max_length=20, unique=True, blank=True,
        validators=[RegexValidator('^[a-z0-9]+$', _('Club code name must be made of characters and/or numbers.'))])
    name = models.CharField(max_length=200, unique=True)
    is_public = models.BooleanField(verbose_name=_('publicly visible'), db_index=True, default=False)
    executives = models.ManyToManyField('Profile', verbose_name=_('executives'), blank=True)
    description = models.TextField(blank=True, help_text=_('A description of the club.'))
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        permissions = (
            ('change_is_public_club', 'Change is_public field for clubs'),
        )
        verbose_name = _('club')
        verbose_name_plural = _('clubs')


class Profile(models.Model):
    user_name = models.OneToOneField(User, verbose_name=_('Username'), on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, blank=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('First name must be made of characters only.'))],
        null=True)
    second_name = models.CharField(max_length=200, blank=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('Second name must be made of characters only.'))],
        null=True)
    self_description = models.TextField(verbose_name=_('self description'), null=True, blank=True)
    clubs = SortedManyToManyField(Club, verbose_name=_('club'), blank=True)

    def __str__(self):
        if self.user_name:
            return str(self.user_name)
        return self.user.username

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')
