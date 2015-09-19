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
        action = ""
        args = urlparse.parse_qs(self.request.uri)
        try:
            mocp_action = args.get("mocp_action")[0]
            shell_action = mocp_actions[mocp_action]
            if os.system(shell_action):
                raise Exception
            action = "$('#status_div').html('success')"
        except:
            action = "$('#status_div').html('failure')"
            print(args, 'faliure')
        self.write(action)


if __name__ == "__main__":
    try:
        script, serve_address, port = argv
        port = int(port)
    except:
        usage(argv[0])

    application = tornado.web.Application([
            (r"/", MainHandler),
    ])
    application.listen(port, address=serve_address)
    tornado.ioloop.IOLoop.current().start()
