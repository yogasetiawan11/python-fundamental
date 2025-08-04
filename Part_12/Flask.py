from flask import Flask

# Creating a flask application instance
app = Flask(__name__)

# Decorator
''' The line @app.route("/") is a route decorator in Flask.
It tells Flask: “When someone visits the root URL (/), run the hello() function.”
'''
@app.route("/")
def hello():
    return 'Yoga setiawan'

app.run('0.0.0.0')