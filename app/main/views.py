from flask import render_template,redirect, url_for
from . import main

#views

@main.route('/')
def index():
    return render_template ('index.html')


@main.route('/post')
def post():
    return render_template ('post.html')


@main.route('/about')
def about():
    return render_template ('about.html')


@main.route('/contact')
def contact():
    return render_template ('contact.html')
