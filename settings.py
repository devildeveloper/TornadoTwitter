import os


DEBUG = False
XSRF_COOKIES = True
COOKIE_SECRET = 'sdesirweory&#)#"$)""YEYWDwhdjfsefsesfdsfjkfljf'
LOGIN_URL = '/login'

_local_path = os.path.dirname(__file__)
STATIC_PATH = os.path.join(_local_path, 'static')
STATIC_URL_PREFIX = '/static/'
DATABASE_DSN = ''
TEMPLATE_PATH = os.path.join(_local_path, 'templates')


try:
    from local_settings import *  # NOQA
except ImportError:
    pass
