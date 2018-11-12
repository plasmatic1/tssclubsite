import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from sortedm2m.fields import SortedManyToManyField

__all__ = ['Club', 'Profile']

class Club(models.Model):
    code = models.CharField(max_length=20, unique=True, blank=True,
        validators=[RegexValidator('^[a-z0-9]+$', _('Club code name must be made of characters and/or numbers.'))])
    name = models.CharField(max_length=200, unique=True, blank=True)
    is_public = models.BooleanField(db_index=True, default=False,
        verbose_name=_('publicly visible'))
    executives = models.ManyToManyField('Profile', blank=True,
        verbose_name=_('executives'),
        help_text=_('The users who are able to edit the details of this club.'))
    description = models.TextField(blank=True,
        help_text=_('A description of the club.'))
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
    user_name = models.OneToOneField(User, on_delete=models.CASCADE, null=True,
        verbose_name=_('Username'))
    first_name = models.CharField(max_length=200, blank=True, null=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('First name must be made of characters only.'))])
    last_name = models.CharField(max_length=200, blank=True, null=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('Second name must be made of characters only.'))])
    self_description = models.TextField(blank=True, null=True,
        verbose_name=_('self description'))
    clubs = SortedManyToManyField('Club', blank=True,
        verbose_name=_('club(s)'))

    def __str__(self):
        if self.user_name:
            return str(self.user_name)
        return self.user.username

    def __unicode__(self):
        return self.user.username

    class Meta:
        permissions = (
            ('edit_joined_clubs', 'Change clubs field for user profile'),
        )
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')
