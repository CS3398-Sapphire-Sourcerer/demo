from flask import Flask
import flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    usernames = 'bobby hill'
    show = 'king of the hill'
    state = 'texas'
    return flask.render_template('home.html', username=usernames, show=show, state=state)


if __name__ == '__main__':
    app.run()
