import datetime

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Profile(models.Model):
    user_name = models.OneToOneField(User, verbose_name=_('Username'), on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, blank=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('First name must be made of characters only.'))])
    second_name = models.CharField(max_length=200, blank=True,
        validators=[RegexValidator('^[a-zA-Z]+$', _('Second name must be made of characters only.'))])

    def __str__(self):
        if(self.user_name is None):
            return "USER PROFILE DOES NOT EXIST";
        return self.user_name

    class Meta:
        verbose_name = _('user profile')
        db_table = 'user_profile'
