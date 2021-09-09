from flask import Blueprint, render_template, request, redirect, flash, url_for
from app import db
import models

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/api')
def api():
    return "WIP, I'll put sth there one day"
