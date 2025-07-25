from .base import *  # noqa
from .base import env




#production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY",default="9CczSdWIlw",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000"
]