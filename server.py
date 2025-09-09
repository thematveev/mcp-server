from flask import Flask
import random

app = Flask(__name__)


def mcp_handler():
    return str(random.randint(0, 100))


app.add_url_rule('/mcp', view_func=mcp_handler)

if __name__ == "__main__":
    app.run()