from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['RECAPTCHA_PUBLIC_KEY'] = 'google site key'
app.config['RECAPTCHA_PRIVATE_KEY'] = 'google secret key'

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    recaptcha = RecaptchaField()



@app.route('/success')
def success():

	form = SignupForm()

	return render_template('success.html', form=form)


@app.route('/home', methods=['GET', 'POST'])
def home():

	form = SignupForm()

	if form.validate_on_submit():

		return redirect(url_for('success'))


	return render_template('home.html', form=form)





if __name__ == '__main__':

	app.run(debug=True)