import flask
from flask import Flask, render_template
from flask_sse import sse
import redis

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
red = redis.StrictRedis()
app.register_blueprint(sse, url_prefix='/stream')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hello')
def publish_hello():
    data = flask.request.data
    sse.publish({"message": data}, type='greeting')
    return "Message sent!"


from gevent.pywsgi import WSGIServer
# For windows only; use Gunicorn for linux environment

http_server = WSGIServer(("", 5000), app)
http_server.serve_forever()
