from .base import *  # noqa
from .base import env

DATABASES = {"default": env.db("DATABASE_URL", default="sqlite:///db.sqlite3")}




#production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY",default="9CczSdWIlw",)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://0.0.0.0:8080",
    "http://localhost:8080",
]

ALLOWED_HOSTS = ["*"]  # only for local dev



EMAIL_BACKEND="djcelery_email.backends.CeleryEmailBackend"

EMAIL_HOST= env("EMAIL_HOST", default="mailhog")
EMAIL_PORT= env("EMAIL_PORT", default=1025) 
DEFAULT_FROM_EMAIL= env("DEFAULT_FROM_EMAIL", default="xcheche@localhost")
DOMAIN = env("DOMAIN", default="localhost:8000")
SITE_NAME= "Medium API Clone"
