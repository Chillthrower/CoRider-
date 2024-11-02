from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb://mongo:27017/')  
db = client.mydatabase  

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    user_id = str(db.users.insert_one(data).inserted_id)
    return jsonify({'id': user_id, 'name': data['name'], 'email': data['email']}), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = list(db.users.find())  
    for user in users:
        user['_id'] = str(user['_id'])
    return jsonify(users)

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    try:
        user = db.users.find_one({'_id': ObjectId(id)}, {'_id': 0})  
        if user:
            return jsonify(user)
        return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Invalid user ID format'}), 400

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Invalid input data'}), 400

        result = db.users.update_one({'_id': ObjectId(id)}, {'$set': data})
        if result.modified_count:
            return jsonify({'message': 'User updated!'}), 200
        return jsonify({'error': 'User not found or no changes made'}), 404
    except Exception as e:
        return jsonify({'error': 'Invalid user ID format'}), 400

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        result = db.users.delete_one({'_id': ObjectId(id)})
        if result.deleted_count:
            return jsonify({'message': 'User deleted!'}), 200
        return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': 'Invalid user ID format'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
