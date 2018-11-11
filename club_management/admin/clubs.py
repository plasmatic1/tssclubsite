from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext, ugettext_lazy as _

from club_management.models import Club

class ClubAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date',)
    fields = ('code', 'name', 'pub_date', 'executives', 'description', 'creation_date')
