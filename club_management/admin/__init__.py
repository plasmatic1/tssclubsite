from django.contrib import admin

from club_management.admin.clubs import ClubAdmin
from club_management.admin.profile import ProfileAdmin
from club_management.models import Profile, Club

admin.site.register(Club, ClubAdmin)
admin.site.register(Profile, ProfileAdmin)
