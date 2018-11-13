from django.contrib import admin

from club_management.admin.profile import ProfileAdmin
from club_management.admin.club import ClubAdmin
from club_management.admin.announcement import AnnouncementAdmin
from club_management.models import Profile, Club, Announcement

admin.site.register(Club, ClubAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Announcement, AnnouncementAdmin)
