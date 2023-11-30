import os
import socket

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    html = "<h3>Hello {name}! version 2.0</h3>" "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
