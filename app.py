import logging
import json
from flask import Flask, jsonify, request

from flask import Flask
from flask_cors import CORS

import uuid

app = Flask(__name__)
CORS(app, resources={r"/users/*": {"origins": "*"}})

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the path to the JSON file
USERS_FILE = 'users.json'

# Function to load users from JSON file


def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save users to JSON file


def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

# GET all users


@app.route('/users', methods=['GET'])
def get_users():
    logger.info("GET all users requested")
    users = load_users()
    return jsonify(users)

# GET a single user by ID


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    logger.info(f"GET user with ID: {user_id}")
    users = load_users()
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        logger.warning(f"User with ID {user_id} not found")
        return jsonify({"error": "User not found"}), 404

# POST a new user


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    logger.info("POST request received to create a new user")
    users = load_users()

    # Generate a UUID for the "id" field
    new_user = {
        "id": str(uuid.uuid4()),  # Generate UUID
        "first_name": data.get("first_name"),
        "last_name": data.get("last_name"),
        "email": data.get("email")
    }
    users.append(new_user)
    save_users(users)
    logger.info("New user created successfully")
    return jsonify(new_user), 201

# PUT/update an existing user by ID


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    logger.info(f"PUT request received to update user with ID: {user_id}")
    users = load_users()
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        data = request.get_json()
        user.update({
            "first_name": data.get("first_name", user["first_name"]),
            "last_name": data.get("last_name", user["last_name"]),
            "email": data.get("email", user["email"])
        })
        save_users(users)
        logger.info(f"User with ID {user_id} updated successfully")
        return jsonify(user)
    else:
        logger.warning(f"User with ID {user_id} not found")
        return jsonify({"error": "User not found"}), 404

# DELETE a user by ID


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    logger.info(f"DELETE request received to delete user with ID: {user_id}")
    users = load_users()
    users = [user for user in users if user['id'] != user_id]
    save_users(users)
    logger.info(f"User with ID {user_id} deleted successfully")
    return jsonify({"message": "User deleted successfully"})


# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True, port=8888)
