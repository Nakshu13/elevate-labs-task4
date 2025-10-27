from flask import Flask, jsonify, request
app = Flask(__name__)
users = []
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "email": data.get("email")
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    for user in users:
        if user["id"] == user_id:
            user["name"] = data.get("name", user["name"])
            user["email"] = data.get("email", user["email"])
            return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({"message": "User deleted"}), 200
    return jsonify({"message": "User not found"}), 404
if __name__ == "__main__":
    app.run(debug=True)
