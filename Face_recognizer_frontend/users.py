from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_mysqldb import MySQL
from flask_cors import cross_origin
from flask_sqlalchemy import SQLAlchemy
from sql.models import Admin

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
# MySQL configurations
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Admin@123'
app.config['MYSQL_DB'] = 'testing'

mysql = MySQL(app)

class UsersResource(Resource):
    @cross_origin()
    def get(self):
        try:
            cur = mysql.connection.cursor()
            cur.execute('SELECT * FROM sql_admin')
            rows = cur.fetchall()
            cur.close()
            return jsonify(rows)
        except Exception as e:
            print('Error fetching users:', e)
            return jsonify(error='Internal Server Error'), 500

@app.route('/api/users', methods=['POST'])
def add_admin():
    data = request.get_json()

    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    new_admin = Admin(admin_username=data['admin_username'])
    db.session.add(new_admin)
    db.session.commit()

    return jsonify({'message': 'Author added successfully'}), 201

api.add_resource(UsersResource, '/api/users')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

