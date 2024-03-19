from flask import Flask, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET"])
def proxy():
    url = request.args.get('url', '')
    encoding = request.args.get('encoding', 'utf-8')
    if url == '':
        return "parameter `url` is required", 400
    response = requests.get(url)
    response.encoding = encoding
    return response.text
