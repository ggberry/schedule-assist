from flask import Blueprint, request, session, render_template, jsonify

index_page = Blueprint('login_page', __name__)

@index_page.route('/', methods=['GET'])
def index():
    #session["classes"] = dict()
    if not "classes" in session:
        classes = dict()
        session['classes'] = classes

    return render_template("index.html", classes=session["classes"])

@index_page.route('/add-class', methods=['POST'])
def add_class():
    form_input = request.form.get("class-input-box")
    classes = session.get("classes", dict())

    if len(classes.keys()) == 0:
        classes["0"] = form_input
    else:
        new_id = max([int(key) for key in classes.keys()]) + 1
        classes[str(new_id)] = form_input

    session["classes"] = classes

    return '', 204

@index_page.route('/remove-class', methods=['POST'])
def remove_class():
    form_input = request.form.get("class-remove")
    classes = session.get("classes", dict())

    del classes[form_input]
    new_classes = dict()

    index = 0
    for _class in classes.values():
        new_classes[index] = _class
        index += 1

    session["classes"] = new_classes

    return '', 204
