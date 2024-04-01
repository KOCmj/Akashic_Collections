from flask import Blueprint, render_template, session
from flask import flash, redirect, url_for, request, json

from flask_login import login_user, logout_user, LoginManager, current_user, login_required


site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/search', methods =['POST'])
def search():
    if request.method == 'POST':
        book_image = request.form.get('book_image')
        if book_image:
            return render_template('searched.html', book_image=book_image)
        else:
            flash('Enter a valid search', 'warning')
            return redirect(url_for('site.home'))

@site.route('/searched/<book_image>')
def searched(book_image):
    return render_template('searched.html', book_image=book_image)

@site.route('/akashic-card')
def membership():
    return render_template('membership.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/imagine')
def imagine():
    return render_template('imagine.html')

