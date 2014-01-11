import tornado
from tornado.options import define, options, parse_command_line
from jinja2 import Environment, FileSystemLoader
from sqlalchemy import create_engine


import settings
from urls import urls


global_settings = {}


class Application(tornado.web.Application):

    def __init__(self, handlers=None, default_host='', transforms=None,
                 wsgi=False, **settings):

        super(Application, self).__init__(handlers, default_host, transforms,
                                          wsgi, **settings)

        self._template_env = Environment(
            loader=FileSystemLoader(self.settings.get('template_path')),
            auto_reload=self.settings.get('debug')
        )
        self._db_engine = create_engine(
            self.settings.get('database_dsn')
        )


# genera diccionario de las variables con mayuscula del archivo settings
for setting in dir(settings):  # genera diccionario
    if setting.isupper():
        global_settings.update({setting.lower(): getattr(settings, setting)})

if __name__ == '__main__':
    define('host', default='127.0.0.1', help='host address to listen on')
    define('port', default=8888, type=int, help='port to listen on')

    parse_command_line()  # parse args en la linea de comandos

    application = Application(urls, **global_settings)
    application.listen(options.port, options.host)
    tornado.ioloop.IOLoop.instance().start()
