import tornado.web
import tornado.escape
from sqlalchemy.orm import sessionmaker


class RequestHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        self._db = None
        super(RequestHandler, self).__init__(application, request, **kwargs)

    @property  # con esto lo llamo como propiedad y no como metodo
    def db(self):
        if not self._db:
            self._db = sessionmaker(
                bind=self.application._db_engine
            )()
        return self._db

    def get_current_user(self):
        user = self.get_secure_cookie('user')
        if user is None:
            return None
        return tornado.escape.json_decode(user)

    def render_string(self, template_name, **kwargs):
        kwargs.update({'handler': self})
        return self.application._template_env.get_template(template_name)\
            .render(**kwargs)

    def render(self, template_name, **kwargs):
        self.finish(self.render_string(template_name, **kwargs))

        def finish(self, chunk=None):
            if self._db:
                self._db.close()
                self._db = None

            super(RequestHandler, self).finish(chunk)
