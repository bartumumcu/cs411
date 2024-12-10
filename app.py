from flask import Flask, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = 'your_secret_key'  


class LoginForm(FlaskForm):
    email= StringField('E-mail')
    mrsId = StringField('openMRS-ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        mrsId = form.mrsId.data
        password = form.password.data
        
        
        if mrsId == 'admin' and password == 'password':  
            flash('Login successful!', 'success')
            return redirect(url_for('two_factor_auth'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    form = LoginForm()
    if request.method == 'POST':
        
        pass
    return render_template('forgot-password.html',form=form)  

@app.route('/two-factor-auth', methods=['GET', 'POST'])
def two_factor_auth():
    if request.method == 'POST':
        code = request.form.get('code')  
        if code == "123":  
            flash('Login successful!', 'success')
            return redirect(url_for('success')) 
        else:
            flash('Invalid code. Please try again.', 'danger')

    return render_template('two_factor_auth.html')  


@app.route('/success')
def success():
    return "Welcome to the OpenMRS system!"

if __name__ == '__main__':
    app.run(debug=True)
