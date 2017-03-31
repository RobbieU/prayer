# -*- coding: utf-8 -*-
from gluon.contrib.heroku import get_db
db = get_db(name=None, pool_size=10)
db.define_table('person',
          Field("enter_your_email", requires = IS_EMAIL(error_message='invalid email!'))),
