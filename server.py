from http.server import HTTPServer

from server import GiftDraw1000Server

hostName = "localhost"
serverPort = 8080

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), GiftDraw1000Server)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
