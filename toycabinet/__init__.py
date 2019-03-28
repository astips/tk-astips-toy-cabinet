# -*- coding: utf-8 -*-

__name__ = 'ToyCabinet'
__version__ = '1.0.0'
__author__ = 'astips'
__package__ = 'toycabinet'
__build__ = 'Cython 0.29, build on March 27, 2019'


import os
import sys
from .const import CONTEXT_CONST
from .core.dborm.const import db_sql


if CONTEXT_CONST.system not in ('windows', 'linux'):
    raise SystemError

sys.path.append(os.path.join(os.path.dirname(__file__), '3rd'))
sys.path.append(os.path.join(os.path.dirname(__file__), '3rd', CONTEXT_CONST.system))


db_sql(False)
