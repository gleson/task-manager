from email.policy import default
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

CHOICES = [('primary', 'Primary'), ('secondary', 'Secondary'), ('success', 'Success'), ('danger', 'Danger'), ('warning', 'Warning'), ('info', 'Info'), ('light', 'Light'), ('dark', 'Dark')]

class AddTaskForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	color = SelectField('Color', choices=CHOICES, default='light')
	text = TextAreaField('Text', default='')
	submit = SubmitField('Submit')


class DeleteTaskForm(FlaskForm):
	submit = SubmitField('Delete')
