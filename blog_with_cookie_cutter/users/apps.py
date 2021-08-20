from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "blog_with_cookie_cutter.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import blog_with_cookie_cutter.users.signals  # noqa F401
        except ImportError:
            pass
