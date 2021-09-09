from flask import Blueprint, render_template, request, redirect, flash, url_for
from app import db
import models

bp = Blueprint('subscriptions', __name__, url_prefix='/subscriptions')


@bp.route('/addSubscription')
def add_subscription():
    return render_template('addsubscription.html')


@bp.route('/showSubscription')
def show_subscription():
    return render_template('showsubscription.html')


@bp.route('/browseSubscriptionTypes')
def browse_subscription_types():
    return render_template('browsesubscriptiontypes.html')


@bp.route('/addSubscriptionType')
def add_subscription_type():
    return render_template('addsubscriptiontype.html')