from flask_wtf import Form
from wtforms.fields import TextField
from wtforms.validators import DataRequired, Email

class EmailPasswordForm(Form):
 name = TextField('Name', validators=[DataRequired()])
 email = TextField('Email', validators=[DataRequired(), Email()]) 
 subject = TextField('Subject', validators=[DataRequired()])
 message = TextField('Type Your Message', validators=[DataRequired(), Email()]) 