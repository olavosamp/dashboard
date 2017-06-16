from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm # import our LoginForm class from forms.py

variableTest = 'Wololo'

# index page
@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Juan'}
	posts = [
		{
			'author': {'nickname': 'John', 'age': 14},
			'body': 'Beautiful day in Lwów'			
		},
		{
			'author': {'nickname': 'Susan', 'age': 22},
			'body': '1453 worst year of my life!'
		},
		{
			'author': {'nickname': 'Jorge', 'age': 32},
			'body': 'I will live to see the Byzantine Empire restored to its former glory'
		},
		{
			'author': {'nickname': 'Adolf', 'age': 9},
			'body': 'We made our last stand at Brno. The fields were painted red at the end of that day'
		}
	]

	return 	render_template('index.html' ,
			title=variableTest,
			user=user,
			posts=posts)

# Login page
# methods=... means that this view function accepts GET and POST requests
@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %(form.openid.data, str(form.remember_me.data)))
		return redirect('/index')

	return render_template('login.html',
							title='Sign In',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])