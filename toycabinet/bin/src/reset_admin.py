# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
)
import toycabinet
import peewee
from toycabinet.core.dborm.models import User
from toycabinet.core.preset import Preset


if not len(Preset.tool.email):
    raise KeyError('ToyCabinet register need client email address, please fill in [presets.json]')

if Preset.tool.db_type == 'postgres':
    DB = peewee.PostgresqlDatabase(**Preset.tool.db_info)
elif Preset.tool.db_type == 'mysql':
    DB = peewee.MySQLDatabase(**Preset.tool.db_info)
elif Preset.tool.db_type == 'sqlite':
    DB = peewee.SqliteDatabase(**Preset.tool.db_info)
else:
    raise KeyError('ToyCabinet support database types: 1.postgres  2.mysql  3.sqlite ')

database = DB
database.connect()

user = User.get(id=1)
user.name = 'admin'
user.admin = True
user.password = '2ff7ffc83a9875f5f0e4957eddf452d928cb1e23'
user.save()
