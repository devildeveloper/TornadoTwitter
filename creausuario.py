import models
import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib
session = sessionmaker(bind=create_engine(settings.DATABASE_DSN))()
user = models.User()
user.name = u'Usuario Prueba'
user.username = 'usuario'
user.password = hashlib.sha1('password').hexdigest()
session.add(user)
try:
    session.commit()
except:
    pass
