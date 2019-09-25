import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from datetime import datetime
from random import randrange
from time import sleep

num_message = 100
time = 0.1

class MyWebSocketServer(tornado.websocket.WebSocketHandler):
    def open(self):
        print('Connection opened')

    def on_message(self, message):

        print('Message Received: %s' % message)
        for message in range(num_message):
            date = datetime.now().isoformat()
            value = randrange(0, 101, 2)
            self.write_message("{\"type\": \"data\", \"payload\": {\"data\": {\"attributes\": {\"device\": \"sys/tg_test/1\", \"attribute\": \"double_scalar\", \"value\": "+value.__str__()+", \"writeValue\": 0.0, \"timestamp\": \""+date+"\"}}}}")
            print("{\"type\": \"data\", \"payload\": {\"data\": {\"attributes\": {\"device\": \"sys/tg_test/1\", \"attribute\": \"double_scalar\", \"value\": \""+value.__str__()+"\", \"writeValue\": 0.0, \"timestamp\": \""+date+"\"}}}}")
            sleep(time)

    def on_close(self):
        print('Connection closed')
    def check_origin(self, origin):
        return True
application = tornado.web.Application([
    (r'/websocketserver', MyWebSocketServer),
])
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(1234)
    tornado.ioloop.IOLoop.instance().start()