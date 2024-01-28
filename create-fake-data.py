import json
import uuid
import hashlib  # Import hashlib library for MD5 hash
from faker import Faker

fake = Faker()


def generate_users_data():
    """
    Generate data for 1000 users.

    Returns:
        list: A list of dictionaries containing user data.
    """
    users = []
    for _ in range(1000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()

        # Calculate MD5 hash of First Name, Full Name, and Email
        namehash = hashlib.md5(
            f"{first_name}{last_name}{email}".encode()).hexdigest()

        user = {
            "id": str(uuid.uuid4()),  # Generate a unique UUID for each user
            "first_name": first_name,  # Generate a random first name
            "last_name": last_name,  # Generate a random last name
            "email": email,  # Generate a random email address
            "namehash": namehash  # Add MD5 hash to user data
        }
        users.append(user)
    return users


def write_to_json_file(users_data):
    """
    Write user data to a JSON file.

    Args:
        users_data (list): A list of dictionaries containing user data.
    """
    with open('users.json', 'w') as f:
        # Write data to JSON file with indentation
        json.dump(users_data, f, indent=4)


if __name__ == "__main__":
    users_data = generate_users_data()  # Generate user data
    write_to_json_file(users_data)  # Write user data to JSON file
