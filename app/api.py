from flask import request, jsonify, render_template, redirect
from app import app, db
from models import Person, Task, Project


# ------------------------------------------------
# HOME ROUTES
# ------------------------------------------------

# GET /
@app.route('/', methods=['GET'])
def get_home():
    return render_template('home.html')


# ------------------------------------------------
# TASK ROUTES
# ------------------------------------------------

# GET /tasks
@app.route('/tasks', methods=['GET'])
def all_tasks():
    data = Task.query.all()
    all_tasks = [item.serialize() for item in data]
    return render_template('tasks.html', tasks=all_tasks)


# GET /tasks/{id},
# DELETE /tasks/{id}
@app.route('/tasks/<int:task_id>', methods=['GET', 'DELETE'])
def get_or_delete_one_task(task_id):
    data = Task.query.get(task_id)

    if request.method == 'DELETE':
        db.session.delete(data)
        db.session.commit()
        return redirect('/tasks')
    else:
        one_task = data.serialize()
        return render_template('tasks.html', tasks=[one_task])


# PUT /tasks/{id}/complete
@app.route('/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    data = Task.query.get(task_id)
    data.completed = True
    db.session.commit()
    return redirect('/tasks')


# ------------------------------------------------
# PROJECT ROUTES
# ------------------------------------------------

# GET /projects
@app.route('/projects', methods=['GET'])
def all_projects():
    data = Project.query.all()
    all_projects = [item.serialize() for item in data]
    return jsonify(all_projects)


# GET /projects/{id}
@app.route('/projects/<int:project_id>', methods=['GET'])
def get_one_project(project_id):
    data = Project.query.get(project_id)
    one_project = data.serialize()
    return jsonify(one_project)


# ------------------------------------------------
# PERSON ROUTES
# ------------------------------------------------

# GET /projects
@app.route('/persons', methods=['GET'])
def all_persons():
    data = Person.query.all()
    all_persons = [item.serialize() for item in data]
    return jsonify(all_persons)


# GET /projects/{id}
@app.route('/persons/<int:person_id>', methods=['GET'])
def get_one_person(person_id):
    data = Person.query.get(person_id)
    one_person = data.serialize()
    return jsonify(one_person)