# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
)
import toycabinet
import peewee
from toycabinet.core.dborm.models import *
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

print 'DB-CONNECT: ', '\n\tSUCCESS'
print 'DB-CONNECTION: '
print '\t{0}'.format(database.connection())

database.create_tables(
    [
        User, Market, Cabinet, Toy, Tag, TagGroup,
        TagGroupConnection, TagToyConnection, Authentication
    ]
)

print 'DB-CREATE-TABLES: ', '\n\tSUCCESS'
tables = database.get_tables()
print 'DB-TABLES:'
for table in tables:
    print '\t{0}'.format(table)

users = User.select()
if not users.count():
    user = User.create(name='admin', admin=True)

clients = Authentication.select()
if not clients.count():
    client = Authentication.create()

print 'DB-CREATE-ADMIN-USER: ', 'SUCCESS'
print 'DB-USER-ADMIN:\n\tName: admin\n\tPassword: 123456'
print ''
print 'DB-INIT: DONE!'
