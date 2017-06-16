from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

# DataRequired is a validator. It checks if the field is not empty
# String and Boolean Field classes are form fields
class LoginForm(Form):
	openid = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)