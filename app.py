from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/canteenmanager'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run()

import auth, clients, subscriptions, configure, api

app.register_blueprint(auth.bp)
app.register_blueprint(clients.bp)
app.register_blueprint(subscriptions.bp)
app.register_blueprint(configure.bp)
app.register_blueprint(api.bp)

db.create_all()


@app.route('/')
def index():
    return render_template('mainpage.html')
