#!flask/bin/python
from flask import Flask, request
import os

app = Flask(__name__)

request_counters = {"POST": 0, "GET": 0}

@app.route('/', methods=["POST", "GET"])
def index():
    env = os.getenv("env", "not set")
    if request.method == "POST":
        request_counters["POST"] += 1
    elif request.method == "GET":
        request_counters["GET"] += 1
    return f"""
            This is {env}!!!<br>
            Our GET counter is: {request_counters['GET']}<br>
            Our POST counter is: {request_counters['POST']}<br>
            Thanks and dont forget to post once in a while :)"""


if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')