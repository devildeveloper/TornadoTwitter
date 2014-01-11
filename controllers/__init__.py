import tornado.web


class RequestHandler(tornado.web.RequestHandler):

    def render_string(self, template_name, **kwargs):
        return self.application._template_env.get_template(template_name)\
            .render(**kwargs)

    def render(self, template_name, **kwargs):
        self.finish(self.render_string(template_name, **kwargs))
