from django.contrib import admin
from .models import User
from .models import Friend
from .models import Event
from .models import Information
from .models import AdjustingSchedule
# Register your models here.

admin.site.register(User)
admin.site.register(Friend)
admin.site.register(Event)
admin.site.register(Information)
admin.site.register(AdjustingSchedule)