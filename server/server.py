from http.server import BaseHTTPRequestHandler
import config
from server import RandomDrawer


class GiftDraw1000Server(BaseHTTPRequestHandler):

    random_drawer = RandomDrawer(config.seed)
    draw = random_drawer.create_draw(config.participants)

    with open('participants.txt', 'w') as file:
        for name, name_hash in draw:
            file.write("{} - {}\n".format(name, name_hash))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>giftdraw1000</title></head>", "utf-8"))

        receiver = GiftDraw1000Server.random_drawer.get_recipient(self.get_name_hash(self.path))

        if self.path[:5] == '/chuj' and receiver is not None:
            self.wfile.write(bytes("<p>dajesz prezent: %s</p>" % receiver, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else:
            self.wfile.write(bytes("<p>cos zjebal*s</p>", "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))

    @staticmethod
    def get_name_hash(path):
        return path[6:]
