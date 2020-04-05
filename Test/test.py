import os
from flask import Flask
from flask_ngrok import run_with_ngrok
import Osnova

app = Flask(__name__)
run_with_ngrok(app)


if __name__ == '__main__':
    Osnova.run()