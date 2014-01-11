from wtforms import Form, TextField, PasswordField
from wtforms.validators import Required, Length


class Login(Form):
    username = TextField(u'Nombre de Usuario', validators=[
        Required('Campo Requerido')
    ])
    password = PasswordField('Password', validators=[
        Required('Campo Requerido')
    ])


class Tweet(Form):
    message = TextField('Tweet', validators=[
        Required('Campo Requerido'),
        Length(max=140, message='up to 140 chars')
    ])


class MultiDict(object):

    def __init__(self, handler):
        self.handler = handler

    def __iter__(self):
        return iter(self.handler.request.arguments)

    def __len__(self):
        return len(self.handler.request.arguments)

    def __contains__(self, name):
        return (name in self.handler.request.arguments)

    def getlist(self, name):
        return self.handler.get_arguments(name, strip=False)
