import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from datetime import datetime
from random import randrange
from time import sleep
import json

num_message = 100
time = 0.4


class MyWebSocketServer(tornado.websocket.WebSocketHandler):
    def open(self):
        print('Connection opened')

    def on_message(self, message):
        data = json.loads(message)
        devices = data['payload']['variables']['fullNames']

        for message in range(num_message):
            for device in devices:
                data = device.split('/')
                device = data[0] + '/' + data[1] + '/' + data[2]
                attribute = data[3]
                if attribute != "Status" and attribute != "string_scalar":
                    print(device +  " - " +attribute)
                    date = datetime.now().isoformat()
                    value = randrange(0, 101, 2)
                    self.write_message(
                        "{\"type\": \"data\", \"payload\": {\"data\": {\"attributes\": {\"device\": \""
                        + device + "\", \"attribute\": \"" + attribute + "\", \"value\": " + value.__str__() +
                        ", \"writeValue\": 0.0, \"timestamp\": \"" + date + "\"}}}}")
            sleep(0.1) #default value between websocket messages
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