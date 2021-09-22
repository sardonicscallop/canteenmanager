from flask import Blueprint, render_template, request, redirect, flash, url_for, g, session
from app import db
from toolbar import ToolbarItem
import models

bp = Blueprint('clients', __name__, url_prefix='/clients')


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id", 0)

    if user_id is None:
        g.user = None
    else:
        g.user = models.User.query.filter_by(id=user_id).first()


@bp.route('/browse')
def browse_clients():
    toolbar = (
        ToolbarItem("icon_edit-find", "find", "Find...", ""),
        ToolbarItem("icon_list-add", "add", "Add", "clients.add_client"),
        ToolbarItem("icon_document-properties", "show", "View details", "clients.show_client"),
        ToolbarItem("icon_document-edit", "edit", "Edit", "clients.modify_client"),
        ToolbarItem("icon_edit-delete", "delete", "Delete", "clients.delete_client")
    )
    clients = models.Client.query.all()
    return render_template('clients/browse.html', clients=clients, toolbar=toolbar)


@bp.route('/add', methods=('GET', 'POST'))
def add_client():
    page_name = "Add new client"

    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        pesel = request.form['pesel']
        passport_no = request.form['passport_no']
        st_class = request.form['st_class']

        error = None

        if not name:
            error = 'Name is required.'
        elif not surname:
            error = 'Surname is required.'
        elif not pesel and not passport_no:
            error = 'Either PESEL or passport no. is required.'

        if error is None:
            client = models.Client(name, surname, pesel, passport_no, st_class)
            attempts = 0
            while attempts < 5:
                try:
                    db.session.add(client)
                    db.session.commit()
                except db.session.IntegrityError:
                    error = f"Client {client.id} is already registered."
                    print(error)
                    client.new_id()
                    attempts += 1
                else:
                    info = f"Client {client.name} {client.surname} registered successfully with ID {client.id}."
                    flash(info, "success")
                    break

        if error:
            flash(error, "error")
    return render_template("clients/add.html", page_name=page_name)


@bp.route('/show')
def show_client():
    if request.args.get('id'):
        client = models.Client.query.filter_by(id=request.args.get('id')).first_or_404()
        return render_template('clients/show.html', client=client)
    else:
        return "Specify client id"


@bp.route('/delete')
def delete_client():
    return


@bp.route('/modify')
def modify_client():
    return


@bp.route('scan')
def open_scan_mode():
    return render_template('clients/scan.html')
