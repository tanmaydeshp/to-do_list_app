from flask import *
from flask_sqlalchemy import *
from flask_login import *
from datetime import date 
from .models import User, Task
from . import db 

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html', user=current_user)

@views.route('/todos/', methods=['GET', 'POST'])
@login_required
def todos():
    if request.method == "POST":
        description = request.form.get('tasktxt')
        task = Task(text=description, date= date.today(), user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
    return render_template('todos.html', user=current_user)

@views.route('/delete_task/', methods=["POST"])
@login_required
def delete_task():
    taskdict = json.loads(request.data) 
    taskID = taskdict['taskID']
    task = Task.query.get(int(taskID))
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()
            flash("Deleted!")

    return jsonify({})
