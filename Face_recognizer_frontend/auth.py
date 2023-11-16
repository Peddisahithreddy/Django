#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin


app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Admin@123'
app.config['MYSQL_DB'] = 'testing'
app.config["DEBUG"]= True
CORS(app)
@app.route('/login', methods=['GET'])
@cross_origin()
def login():
    form = sql_admin()
    if form.validate_on_submit():
        user = User.query.filter_by(admin_username=form.admin_username.data).first()
        if user and user.admin_password == form.admin_password.data:
    # Passwords match, proceed with the login logic
          flash('Login successful!', 'success')
          return redirect(url_for('user'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login', title='Login', form=form)



    # Validate the username and password here
    # You should have your own logic to verify the credentials



if __name__ == '__main__':
    app.run()
