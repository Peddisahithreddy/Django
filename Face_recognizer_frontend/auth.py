#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Admin@123@3306/testing'
app.config["DEBUG"]= True
CORS(app)
@app.route('/login', methods=['GET','POST'])
def login():
    form = sql_admin()
    if form.validate_on_submit():
        amin_username = User.query.filter_by(admin_username=form.admin_username.data).first()
        if user and bcrypt.check_password_hash(user.admin_password, form.admin_password.data):
            flash('Login successful!', 'success')
            return redirect(url_for('user'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login', title='Login', form=form)


    # Validate the username and password here
    # You should have your own logic to verify the credentials



if __name__ == '__main__':
    app.run()
