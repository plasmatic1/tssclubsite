from django.forms import ModelForm
from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext, ugettext_lazy as _

from club_management.models import Club

class ClubAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date',)
    fields = ('code', 'name', 'is_public', 'executives', 'description', 'creation_date')

    def get_readonly_fields(self, request, obj=None):
        ret = self.readonly_fields
        if not request.user.has_perm('club_management.change_is_public_club'):
            ret += ('is_public',)
        return ret
