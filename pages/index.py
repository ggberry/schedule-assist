from flask import Blueprint, request, render_template

index_page = Blueprint('login_page', __name__)


@index_page.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.get("class-input"))

    return render_template("index.html")
