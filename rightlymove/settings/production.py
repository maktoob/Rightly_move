import dj_database_url

from .base import *

DATABASES = {
    {
        'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    }
}
