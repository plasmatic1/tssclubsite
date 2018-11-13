from django.contrib import admin
from django.forms import ModelForm
from django.utils.translation import ugettext, ugettext_lazy as _

from club_management.models.announcement import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
    fields = ('code', 'title', 'is_public', 'date_posted')
