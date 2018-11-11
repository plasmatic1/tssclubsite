from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext, ugettext_lazy as _

from club_management.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fields = ('user_name', 'first_name', 'second_name', 'self_description', 'clubs')
