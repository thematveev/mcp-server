from flask import Flask, request, jsonify
import random

app = Flask(__name__)


def mcp_handler():
    data = request.json
    print(data)
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
    elif data['method'] == "notifications/initialized":
        return "ok"
    elif data['method'] == "tools/list":
        return jsonify(
            {
                "jsonrpc": "2.0",
                "id": data["id"],
                "result": {
                    "tools": [
                        {
                            "name": "radom_generator",
                            "title": "Randomizer",
                            "description": "Creates real random numbers from 1 to 100",
                            "inputSchema": {
                                "type": "object",
                                "properties": {},
                                "required": []
                            }
                        }
                    ]
                }
            }
        )
    elif data["method"] == "tools/call":
        s = f"REAL RANDOM VALUE IS -> {random.randint(1, 100)}"
        print(s)
        return jsonify(
            {
                "jsonrpc": "2.0",
                "id": data["id"],
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": s
                        }
                    ]
                }
            }
        )


app.add_url_rule('/mcp', view_func=mcp_handler, methods=["POST"])

if __name__ == "__main__":
    app.run()