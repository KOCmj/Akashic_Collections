from forms import UserLoginForm, SignInForm
from models import User, db, check_password_hash
from flask import Blueprint, render_template, request, redirect, url_for, flash

from flask_login import login_user, logout_user, LoginManager, current_user, login_required


auth = Blueprint('auth', __name__, template_folder='auth_templates')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserLoginForm()

    try: 
        if request.method == 'POST' and form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            DOB = form.DOB.data
            email = form.email.data
            password = form.password.data
            

            user = User(first_name, last_name, DOB, email, password=password)


            db.session.add(user)
            db.session.commit()

            flash(f'You have successfully created a user account {email}', 'User-created')
            
            return redirect(url_for('site.home'))
    except:
        raise Exception('Invalid form data: Please check your form')
    return render_template('forms.html', form=form)
    

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()

    try:
        if request.method == 'POST' and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email)

            logged_user = User.query.filter_by(email=email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('Welcome back to the KOC lab!', 'success')
                return redirect(url_for('site.profile'))
            else:
                flash('Failed to enter the KOC Lab', 'auth-failed')
    except ValueError:
        flash('Invalid data: Please check your form')
    return render_template('sign_in.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('site.home'))
