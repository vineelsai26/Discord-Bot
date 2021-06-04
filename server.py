from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.getenv('PORT') or 5000
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def run():
    app.run(port=PORT)
