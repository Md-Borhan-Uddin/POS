from .base import *

INSTALLED_APPS += [
    "django_browser_reload",
    'tailwind',
]

MIDDLEWARE += [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]


TAILWIND_APP_NAME = 'core'

INTERNAL_IPS = [
    "127.0.0.1",
]