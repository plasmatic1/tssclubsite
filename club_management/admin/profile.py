from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext, ugettext_lazy as _

from club_management.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    fields = ('user_name', 'first_name', 'last_name', 'self_description', 'clubs')

    def get_readonly_fields(self, request, obj=None):
        ret = self.readonly_fields
        if not request.user.has_perm('club_management.edit_joined_clubs'):
            ret += ('clubs',)
        return ret;
