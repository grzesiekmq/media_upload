import os, importlib
from flask import Flask
from flask import request, redirect, url_for, render_template, jsonify
from media.naming import generate_name
from ordering.animation_order import AnimationOrder

services = importlib.import_module("services_%s" % (os.environ.get('APP_ENV', 'test')))

app = Flask(__name__)

@app.route("/")
def upload():
    return render_template('upload_file.html')


@app.route("/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files['uploaded_media']
    key = generate_name(uploaded_file.filename)
    services.media_storage.store(key=key, media=uploaded_file)
    return jsonify({
        'key': key
    })


@app.route("/process-order", methods=["POST"])
def process_order():
    order_request = request.get_json(silent=True)
    services.animation_order_bus.handle_order(
        AnimationOrder(email=order_request['email'], photos=order_request['photos'])
    )

    return jsonify({})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
