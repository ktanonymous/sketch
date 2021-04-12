from django.contrib import admin
from .models import Users, RequestLogs, ResponseLogs

admin.site.register(Users)
admin.site.register(RequestLogs)
admin.site.register(ResponseLogs)