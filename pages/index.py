from flask import Blueprint, render_template

index_page = Blueprint('login_page', __name__)

@index_page.route('/', methods=['GET'])
def index():
    return render_template("index.html")
