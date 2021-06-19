from django.contrib import admin
from .models import User
from .models import Friend
from .models import Event
from .models import Information
from .models import AdjustingSchedule


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class FriendAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class InformationAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class AdjustingScheduleAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(User, UserAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Information, InformationAdmin)
admin.site.register(AdjustingSchedule, AdjustingScheduleAdmin)
