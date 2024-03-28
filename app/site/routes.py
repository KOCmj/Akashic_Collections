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
        query = request.form.get('query')
        if query:
            return render_template('searched.html', query=query)
        else:
            flash('Enter a valid search', 'warning')
            return redirect(url_for('site.home'))

@site.route('/searched/<query>')
def searched(query):
    return render_template('searched.html', query=query)

@site.route('/akashic-card')
def membership():
    return render_template('membership.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/imagine')
def imagine():
    return render_template('imagine.html')
