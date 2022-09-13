import flask_sqlalchemy
from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
from datetime import datetime
import forms

CHOICES = {'primary': 'bg-primary text-white', 'secondary': 'bg-secondary text-white', 'success': 'bg-success text-white', 'danger': 'bg-danger text-white', 'warning': 'bg-warning', 'info': 'bg-info', 'light': 'bg-light', 'dark': 'bg-dark text-white'}


@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    colors = CHOICES
    return render_template('index.html', tasks=tasks, colors=colors)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        t = Task(title=form.title.data, color=form.color.data, text=form.text.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        flash('Task added to the database!')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()

    if task:
        if form.validate_on_submit():
            task.title = form.title.data
            task.color = form.color.data
            task.text = form.text.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task has been updated')
            return redirect(url_for('index'))
        form.title.data = task.title
        form.color.data = task.color
        form.text.data = task.text
        return render_template('edit.html', form=form, task_id=task_id)
    
    flash('Task not found!')
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteTaskForm()

    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task has been deleted')
            return redirect(url_for('index'))
        
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)

    flash('Task not found!')
    return redirect(url_for('index'))
