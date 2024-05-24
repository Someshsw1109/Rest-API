from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
import json
import api.cars as cars


class RestHandler(BaseHTTPRequestHandler):
    def respond(self, status_code, message=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if message is not None:
            self.wfile.write(bytes(message, "utf8"))

    def is_body_valid(self, _body, _keys):
        body_keys = set(_body.keys())
        if len(body_keys) != len(_keys):
            return False
        if len([key for key in _keys if key not in _body]) > 0:
            return False
        return True
    def do_GET(self):
        if self.path == "/cars":
            self.respond(HTTPStatus.OK, cars.get_cars())
            return
        try:
            command, resource = self.path[1:].split("/", 1)
        except ValueError: 
            self.respond(HTTPStatus.BAD_REQUEST)
            return
        if command != "car" or resource == "": 
            self.respond(HTTPStatus.BAD_REQUEST)
            return
        car = cars.get_car(resource)
        if car is None: 
            self.respond(HTTPStatus.NOT_FOUND)
            return
        self.respond(HTTPStatus.OK, car)
    def do_POST(self):
        if self.path != "/cars":
            self.respond(HTTPStatus.BAD_REQUEST)
            return
        content_len = int(self.headers.get("content-length", 0))
        post_body = self.rfile.read(content_len)
        try:
            body = json.loads(post_body)
        except json.JSONDecodeError:
            self.respond(HTTPStatus.BAD_REQUEST)
            return
        required_keys = ("id", "make", "model", "year", "price")
        if self.is_body_valid(body, required_keys) is False:
            self.respond(HTTPStatus.UNPROCESSABLE_ENTITY)
            return
        car = cars.get_car(body["id"])
        if car is not None:
            self.respond(HTTPStatus.CONFLICT)
            return
        cars.insert(body)
        self.respond(HTTPStatus.ACCEPTED)
    def do_PUT(self):
        try:
            command, resource = self.path[1:].split("/", 1)
        except ValueError:
            self.respond(HTTPStatus.BAD_REQUEST)
            return
        if command != "car" or resource == "":
            self.respond(HTTPStatus.BAD_REQUEST)
            return
        car = cars.get_car(resource)
        if car is None:
            self.respond(HTTPStatus.NOT_FOUND)
            return
        content_len = int(self.headers.get("content-length", 0))
        post_body = self.rfile.read(content_len)
        try:
            body = json.loads(post_body)
        except json.JSONDecodeError:
            self.respond(HTTPStatus.BAD_REQUEST)
            return
        required_keys = ("make", "model", "year", "price")
        if self.is_body_valid(body, required_keys) is False:
            self.respond(HTTPStatus.UNPROCESSABLE_ENTITY)
            return
        cars.update(resource, body)
        self.respond(HTTPStatus.ACCEPTED)
    def do_DELETE(self):
        try:
            command, resource = self.path[1:].split("/", 1)
        except ValueError:
            self.respond(HTTPStatus.BAD_REQUEST)
            return
        if command != "car" or resource == "":
            self.respond(HTTPStatus.BAD_REQUEST)
            return
        car = cars.get_car(resource)
        if car is None:
            self.respond(HTTPStatus.NOT_FOUND)
            return
        cars.delete(resource)
        self.respond(HTTPStatus.ACCEPTED)
if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 8081
    server_address = (ip, port)
    httpd = HTTPServer(server_address, RestHandler)
    print("Server running at {}:{}".format(ip, port))
    httpd.serve_forever()