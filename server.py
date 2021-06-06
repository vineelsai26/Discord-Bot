from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def run():
    app.run()
