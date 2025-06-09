#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    print(f"This web server is running at {request.remote_addr}")#what is to be ran into the server
    return Response("A WSGI generated this response!")

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple(
        hostname="localhost",   #tells it where to run the server
        port=5555,
        application=application
    )