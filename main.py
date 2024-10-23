import flask


# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    return flask.render_template('index.html')

@APP.route('/put30')
def put30():
    return flask.render_template('put.html')


if __name__ == '__main__':
    APP.debug=True
    APP.run(port=8080)