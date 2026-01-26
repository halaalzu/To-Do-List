from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Task
from . import db
import json
from datetime import datetime


views = Blueprint('views', __name__)


@views.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    return redirect(url_for('auth.login'))


@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        task = request.form.get('task')
        due_date_str = request.form.get('due_date')

        if len(task) < 1:
            flash('Task is too short!', category='error')
        else:
            due_date = None
            if due_date_str:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()

            new_task = Task(
                task=task,
                due_date=due_date,
                user_id=current_user.id
            )

            db.session.add(new_task)
            db.session.commit()
            flash('Task Created!', category='success')

    return render_template("home.html", user=current_user)
@views.route('/delete-task', methods=['POST'])
def delete_task():  
    task = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    taskId = task['taskId']
    task = Task.query.get(taskId)
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()

    return jsonify({})

@views.route("/toggle-task", methods=["POST"])
@login_required
def toggle_task():
    data = json.loads(request.data)
    task = Task.query.get(data["taskId"])

    if task and task.user_id == current_user.id:
        task.completed = not task.completed
        db.session.commit()

    return jsonify({})
