from controllers import RequestHandler


class Main(RequestHandler):

    def get(self):
        self.render('index.html', debug=self.settings.get('debug'))
