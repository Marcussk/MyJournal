from flask import jsonify, request

from myjournal import app
from myjournal.models.user import User

@app.route('/api/users', methods=['GET', 'POST'])
def users_endpoint():
    if request.method == 'GET':
        return get_user_collection()
    elif request.method == 'POST':
        return create_user()

@app.route('/api/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def users_id_endpoint(user_id):
    if request.method == 'GET':
        return get_user(user_id)
    elif request.method == 'PUT':
        return update_user(user_id)
    elif request.method == 'DELETE':
        return delete_user(user_id)

def get_user(user_id: int) -> str:
    """
        Get user by ID
    """
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error' : 'Not Found'}), 404
    else:
        return jsonify(user.serialize())

def get_user_collection() -> str:
    """
        Get all users in collection
    """
    userCollection = []
    for user in User.query.all():
        userCollection.append(user.serialize())
    return jsonify({'users': userCollection})

def create_user() -> str:
    """ Create new user from JSON request """
    if not all(('username', 'email' in request.json)):
        return jsonify({'error': 'Bad Request'}), 500
    for user in User.query.all():
        if user.email == request.json['email']:
            return jsonify({'error': 'Bad Request', 'message': 'user with that email already exists'}), 500
        user = User(
            username=request.json['username'],
            email=request.json['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize())

def update_user(users_id: int) -> str:
    raise NotImplementedError

def delete_user(users_id: int) -> str:
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error' : 'Not Found'}), 404
    else:
        db.session.delete(user)
        db.session.commit()
        return jsonify(user.serialize())