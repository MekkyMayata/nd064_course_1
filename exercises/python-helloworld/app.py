from flask import Flask,json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Mayata says Hello World!"

@app.route("/status")
def status():
    data = { "result": "OK - healthy" }
    response = app.response_class(
        response = json.dumps(data),
        status = 200,
        mimetype = 'application/json'
    )
    return response

@app.route("/metrics")
def metrics():
    data = {
            "data": {
                "UserCount": 140,
                "UserCountActive": 23
            }
        }
    response = app.response_class(
        response = json.dumps(data),
        status = 200,
        mimetype = 'application/json'
    )
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
