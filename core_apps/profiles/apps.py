from django.apps import AppConfig
# Used for translation in python & django to various languages
from django.utils.translation import gettext_lazy as _ 



class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_apps.profiles'
    verbose_name = _("Profiles")
