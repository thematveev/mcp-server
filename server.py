from flask import Flask, request
import random

app = Flask(__name__)


def mcp_handler():
    print(request.data)
    return str(random.randint(0, 100))


app.add_url_rule('/mcp', view_func=mcp_handler, methods=["POST", "GET"])

if __name__ == "__main__":
    app.run()