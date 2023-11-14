from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_mysqldb import MySQL
from flask_cors import cross_origin


app = Flask(__name__)
api = Api(app)

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

api.add_resource(UsersResource, '/api/users')

if __name__ == '__main__':
    app.run(debug=True)

