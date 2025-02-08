#!flask/bin/python
from flask import Flask, request

app = Flask(__name__)

request_counters = {"POST": 0, "GET": 0}

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        request_counters["POST"] += 1
        # return f"Our POST counter is: {request_counters['POST']}\n"
    elif request.method == "GET":
        request_counters["GET"] += 1
        # return f"Our GET counter is: {request_counters['GET']}\n"
    return f"ur GET counter is: {request_counters['GET']}\nOur POST counter is: {request_counters['POST']}\n"

# @app.route('/stats', methods=["GET"])
# def stats():
#     """New route to check request counts"""
#     return f"Our POST counter is: {request_counters['POST']}, and our GET counter is: {request_counters['GET']}.\n"

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')