#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import urllib.parse as urlparse
import os
from sys import argv, exit

mocp_actions = {
    "next"    : "mocp -f",
    "prev"    : "mocp -r",
    "toggle"  : "mocp -G",
    "play"    : "mocp -p",
    "pause"   : "mocp -P",
    "volup"   : "mocp -v +5",
    "voldown" : "mocp -v -5",
}

def usage(cmd):
    print("Usage: %s <address> <port>" % cmd)
    exit(1)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class ControlHandler(tornado.web.RequestHandler):
    def get(self):
        resp = "failure"
        query = urlparse.urlparse(self.request.uri).query
        args = urlparse.parse_qs(query)
        try:
            mocp_action = args.get("mocp_action")[0]
            shell_action = ""
            if mocp_action == "volume_set":
                value = args.get("value")[0]
                shell_action = "mocp -v " + value
            else:
                shell_action = mocp_actions[mocp_action]
            if os.system(shell_action):
                raise Exception
            resp = "success"
        except:
            print(args, 'faliure')
        self.write(resp)

if __name__ == "__main__":
    try:
        script, serve_address, port = argv
        port = int(port)
    except:
        usage(argv[0])

    cwd = os.getcwd()
    application = tornado.web.Application([
            (r"/", MainHandler),
            (r"/control", ControlHandler),
            (r"/(.*\.js)", tornado.web.StaticFileHandler,{"path": cwd }),
    ])
    application.listen(port, address=serve_address)
    tornado.ioloop.IOLoop.current().start()
