from tornado.web import url  # no es un metodo registrado pero funca

import controllers.main


urls = [
    url(
        '/',
        controllers.main.Main,
        name='index'
    ),
    url(
        '/login',
        controllers.main.Login,
        name='login'
    ),
    url(
        'logout',
        controllers.main.Logout,
        name='logout'
    )
]
