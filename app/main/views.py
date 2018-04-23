from flask import render_template,redirect, url_for
from . import main
from flask_login import login_required,current_user
from ..models import User,Posts,Comments,Subscription
import markdown2
from ..import db
from flask_admin.contrib.sqla import ModelView
from .forms import PostsForm,CommentsForm,SubscriptionForm
from flask_admin import Admin

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



