"""このファイルは気にせずとも良い
アプリケーション構成クラスを設定
settings.py の INSTALLED_APPS に追加することで、アプリケーション構成クラスを登録
"""

from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'base'
