import flask
import custom_flask_sse
import gevent.monkey; gevent.monkey.patch_all()

app = flask.Flask(__name__)
channel = custom_flask_sse.Channel()


@app.route('/')
def index():
    return flask.render_template("index_without_redis.html")


def format_sse(data: str, event_type: str):
    return f'event: {event_type}\ndata: {data}\n\n'


@app.route('/publish', methods=['POST'])
def publish():
    data = flask.request.data.decode('utf-8')
    print(f'publish: {data}')
    channel.publish(data, 'my_custom_event_type')
    return "OK"


@app.route('/subscribe')
def subscribe():
    # return flask.stream_with_context(channel.subscribe())
    return channel.subscribe()


# @app.route('/stream', methods=['PUT'])
# def stream():
#     data = flask.request.data.decode()
#     output_data = format_sse(data, 'greeting')
#     print(output_data)
#     # def eventStream():
#     #     while True:
#     #         yield f'data: {data}\n\n'
#     # # threading.Thread(target=eventStream).start()
#     return flask.Response(output_data, mimetype="text/event-stream")


# For windows only; use Gunicorn for linux environment
from gevent.pywsgi import WSGIServer
http_server = WSGIServer(("", 5000), app)
http_server.serve_forever()
