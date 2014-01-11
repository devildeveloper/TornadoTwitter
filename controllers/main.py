from controllers import RequestHandler
from sqlalchemy import and_
import hashlib
import tornado.escape


import forms
import models


class Main(RequestHandler):

    @tornado.web.authenticated
    def get(self, form=forms.Tweet()):
        self.render('index.html', form=form)

    @tornado.web.authenticated
    def post(self):
        form = forms.Tweet(forms.MultiDict(self))

        if not form.validate():
            self.get(form)
        else:
            tweet = models.Tweet()
            tweet.message = form.message.data
            tweet.user_id = self.current_user.get('id')
            self.db.add(tweet)
            try:
                self.db.commit()
            except:
                self.db.rollback()
            self.redirect(self.reverse_url('index'))


class Login(RequestHandler):

    def get(self, form=forms.Login()):
        self.render('login.html', form=form)

    def post(self):
        form = forms.Login(forms.MultiDict(self))
        if not form.validate():
            self.get(form)  # esto imprimiria errores de la instancia form
        else:
            user = self.db.query(
                models.User.id
            ).filter(and_(
                models.User.username == form.username.data,
                models.User.password == hashlib.sha1(
                    form.password.data
                ).hexdigest()
            )).first()
            if user is None:
                self.get(form)
            else:
                self.set_secure_cookie('user', tornado.escape.json_encode({
                    'id': user.id
                }))
                self.redirect(self.get_argument(
                    'next',
                    self.reverse_url('index'))
                )


class Logout(RequestHandler):

    def get(self):
        self.clear_all_cookies()
        self.redirect(self.reverse_url('index'))
