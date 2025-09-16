from flask import Flask, request, jsonify
import random

app = Flask(__name__)


def mcp_handler():
    data = request.json()
    if data['method'] == "initialize":
        return jsonify({
          "jsonrpc": "2.0",
          "id": data["id"],
          "result": {
            "protocolVersion": data["params"]["protocolVersion"],
            "capabilities": {
              "tools": {
                "listChanged": False
              },
              "resources": {}
            },
            "serverInfo": {
              "name": "flask-server",
              "version": "1.0.1"
            }
          }
        })


app.add_url_rule('/mcp', view_func=mcp_handler, methods=["POST"])

if __name__ == "__main__":
    app.run()