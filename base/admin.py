from django.contrib import admin
from .models import User
from .models import Friend
from .models import Information
# Register your models here.

admin.site.register(User)
admin.site.register(Friend)
admin.site.register(Information)