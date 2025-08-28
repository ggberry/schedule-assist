from flask import Flask

from pages.index import index_page

app = Flask(__name__)
app.register_blueprint(index_page)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return response

if __name__ == '__main__':
    app.run(debug=True)
