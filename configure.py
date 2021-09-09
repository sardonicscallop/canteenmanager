from flask import Blueprint, render_template, request, redirect, flash, url_for
from app import db
import models

bp = Blueprint('configure', __name__, url_prefix='/configure')


@bp.route('/')
def configure():
    return render_template('configure/index.html')


@bp.route('/users')
def users_overview():
    return render_template('configure/users_overview.html')


@bp.route('/users/add')
def users_add():
    return render_template('configure/users_add.html')
