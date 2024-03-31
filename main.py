from flask import Flask, jsonify, request
from db_connector import connect_database
from getUsersData import user_data
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/get_users', methods=['GET'])
def get_users():
    db, cursor = connect_database()
    if db and cursor:
        try:
            id = request.args.get('id')
            name = request.args.get('name')
            email = request.args.get('email')

            users = user_data(cursor, id=id, name=name, email=email)
            return jsonify(users)

        except Exception as e:
            return jsonify({'ERROR': str(e)})
        
        finally:
            cursor.close()
            db.close()
    else:
        return jsonify({'Error': 'Failed to connect to DB'})

if __name__ =='__main__':
    app.run(debug=True)