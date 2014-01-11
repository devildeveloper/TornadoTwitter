from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Unicode, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

Entity = declarative_base()


class User(Entity):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(40), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    tweets = relationship('Tweet')  # apunta a la clase


class Tweet(Entity):
    __tablename__ = 'tweets'

    id = Column(Integer, primary_key=True)
    message = Column(Unicode(140), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # apunta a la columna
    user_id = Column(Integer, ForeignKey('users.id'))


if __name__ == '__main__':
    from sqlalchemy import create_engine

    import settings

    engine = create_engine(
        settings.DATABASE_DSN,
        echo=settings.DEBUG
    )
    Entity.metadata.create_all(engine)
