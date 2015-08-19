#!/usr/bin/env python

import tornado.web
import tornado.ioloop
import json

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

class ThingHandler(tornado.web.RequestHandler):
    def get(self, parent_id, child_id):
        def lst(parent_id):
            self.write("Hello, %s, you're interested in ALL!\n" % (parent_id,))
            self.write("And you gave the 'hello' argument as %s\n" % self.get_argument("hello"))

        def show(parent_id, child_id):
            self.write("Hello, %s, you're interested in %s!\n" % (parent_id, child_id))
            self.write("And you gave the 'hello' argument as %s\n" % self.get_argument("hello"))

        if child_id == "":
            lst(parent_id)
        else:
            show(parent_id, child_id)

    def post(self, parent_id, child_id):
        self.write("Hello, %s, you're interested in %s!\n" % (parent_id, child_id))
        data = json.loads(self.request.body.decode('utf-8'))
        self.write("And you have the 'hello' datum as %s\n" % data['hello'])


application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/v1/parent/([0-9]*)/child/?([0-9]*)", ThingHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
