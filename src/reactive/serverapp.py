"""Tornado Web App"""


import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    """Main Handler"""

    def get(self):
        """Get"""

        self.write("Hello World!\n")


def make_app():
    """ Make App """

    routes = [(r"/", MainHandler)]

    return tornado.web.Application(routes)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
