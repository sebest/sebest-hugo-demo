import os
from eve import Eve

from .settings import DEFAULT_SETTINGS

app = Eve(settings=DEFAULT_SETTINGS)
