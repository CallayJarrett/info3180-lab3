from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired
from wtforms import EmailField
from wtforms import TextAreaField
from wtforms.validators import Email 

class ContactForm(FlaskForm):
        name = StringField('Name', validators=[InputRequired()])
        email = EmailField("E-mail",validators=[InputRequired(),Email()])
        subject = StringField("Subject", validators=[InputRequired()])
        message = TextAreaField("Message", validators=[InputRequired()]) 

