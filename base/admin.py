"""
ダッシュボード（管理者画面）の表示方法や操作の仕方をデフォルトから変更するための設定を行う
"""

from django.contrib import admin

from .models import User, Friend, Event, Information, AdjustingSchedule

# id は変更されたくないため、読み取り専用とする
# 上記は、<モデル名>Admin クラス全てに共通


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


# admin.site.register
# 第一引数 : <モデル名>
# 第二引数 : <モデル名>Admin
# NOTE: 第二引数がなくてもエラーは出ないが、今回は必須！！
admin.site.register(User, UserAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Information, InformationAdmin)
admin.site.register(AdjustingSchedule, AdjustingScheduleAdmin)
