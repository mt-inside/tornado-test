#!/usr/bin/env python

import tornado.web
import tornado.ioloop
import json

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world!")

class ThingHandlerInt(tornado.web.RequestHandler):
    def get(self, parent_id, child_id):
        def lst(parent_id):
            self.write("Hello, %s, you're interested in ALL!\n" % (parent_id,))
            self.write("And you gave the 'hello' argument as %s\n" % self.get_argument("hello"))

        def show(parent_id, child_id):
            self.write("Hello, %s, you're interested in %s!\n" % (parent_id, child_id))
            self.write("And you gave the 'hello' argument as %s\n" % self.get_argument("hello"))

        if child_id is None:
            lst(parent_id)
        else:
            show(parent_id, child_id)

    def post(self, parent_id, child_id):
        assert(child_id == "")
        self.write("Hello, %s, you're interested in making a new child!\n" % (parent_id,))
        data = json.loads(self.request.body.decode('utf-8'))
        self.write("You have the 'hello' datum as %s\n" % data['hello'])

    def delete(self, parent_id, child_id):
        d = dict(status="ok", remaining=1)
        d.update({x : x*2 for x in (1,2,3)})
        # Rendering to JSON seems to be automatic for compound types, including
        #   setting correct response MIME type
        # Outer object must be a dict
        self.write(d)

class ThingHandlerStr(tornado.web.RequestHandler):
    def get(self, parent_id, child_id):
        self.write("Requested by string ID %s\n" % (parent_id,))


application = tornado.web.Application([
    (r"/", IndexHandler),
    # Making the last group optional passes None as that arg if it's not matched
    # Alternatively could rewrite as [0-9]*, in which case there being no element will give ""
    (r"/v1/parent/([0-9]*)/child/?([0-9]+)?", ThingHandlerInt),
    (r"/v1/parent/([a-z]*)/child/?([0-9]+)?", ThingHandlerStr),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
