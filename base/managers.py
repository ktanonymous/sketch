"""ユーザー登録に関する設定をカスタマイズする
"""
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email: str, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        self._set_permission(extra_fields, False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        self._set_permission(extra_fields, True)

        return self._create_user(email, password, **extra_fields)

    @staticmethod
    def _set_permission(extra_fields, is_permitted):
        extra_fields.setdefault('is_staff', is_permitted)
        extra_fields.setdefault('is_superuser', is_permitted)
        extra_fields.setdefault('is_admin', is_permitted)
