import os
from flask import Flask, send_from_directory

from pages.index import index_page

app = Flask(__name__)
app.secret_key = "dsagoat"
app.register_blueprint(index_page)

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response


if __name__ == '__main__':
    app.run(debug=True)
