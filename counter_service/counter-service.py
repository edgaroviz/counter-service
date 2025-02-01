#!flask/bin/python
from flask import Flask, request, request_started

app = Flask(__name__)
post_counter = 0
get_counter = 0
@app.route('/', methods=["POST", "GET"])
def index():
    global post_counter
    global get_counter
    if request.method == "POST":
        post_counter+=1
        return "Hmm, Plus 1 to POST please "
    elif request.method == "GET":
        get_counter+=1
        return "Hmm, Plus 1 to GET please "
    else:
        return str(f"Our POST counter is: {post_counter}, and out GET counter is: {get_counter} ")
if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')
----
#!flask/bin/python
from flask import Flask, request

app = Flask(__name__)

request_counters = {"POST": 0, "GET": 0}

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        request_counters["POST"] += 1
        return f"Our POST counter is: {request_counters['POST']}\n"
    elif request.method == "GET":
        request_counters["GET"] += 1
        return f"Our GET counter is: {request_counters['GET']}\n"

@app.route('/stats', methods=["GET"])
def stats():
    """New route to check request counts"""
    return f"Our POST counter is: {request_counters['POST']}, and our GET counter is: {request_counters['GET']}.\n"

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')