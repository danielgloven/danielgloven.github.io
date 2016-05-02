from flask import flask

app = Flask(__name__)

@app.route('/blog')
def blog():
    return 'This is my blog'

if __name__ == "__main__":
    app.run()
