from .base import *

DATABASES = {
    'default': os.environ.get('DATABASE_URL')
}
