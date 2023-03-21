"""
A simple Flask app for greeting users and serving static files of frontend.
"""

import os
from flask import Flask, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders a simple greeting to the user.
    """
    return 'Hello, World!'


@main.route("/hello", methods=["GET", "POST"])
def hello():
    """
      Możliwość wpisania imienia, aplikacja wyświetli "Hello, (name)!".
       """
    if request.method == "POST":
        name = request.form.get("name")
        return f"Hello, {name}!"
    return render_template("hello.html")


if __name__ == "__main__":
    main.run(debug=True, host="0.0.0.0", port=8080)
