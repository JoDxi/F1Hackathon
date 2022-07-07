from flask import render_template, url_for, flash, redirect
from formulaweb import app
from formulaweb.forms import RegistrationForm, LoginForm
from formulaweb.models import Teams


@app.route('/')
def homepage():
	return render_template('home_page.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f"Account created for {form.username.data}!", 'success')
		return redirect(url_for('homepage'))
	return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)


@app.route('/hallfame')
def halloffame():
	return render_template('hall_fame.html', title='Hall Of Fame')


@app.route('/teams', methods=['GET', 'POST'])
def teams():
	team = Teams.query.order_by(Teams.team_name)
	return render_template('teams.html', title='F1 Teams', team=team)



