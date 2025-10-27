# elevate-labs-task4
⚙️ Flask REST API for User Management

A simple REST API built using Flask to manage user data.
Supports basic CRUD operations — Create, Read, Update, and Delete users.

🚀 Features

GET /users → Retrieve all users

GET /users/<id> → Retrieve a specific user

POST /users → Add a new user

PUT /users/<id> → Update an existing user

DELETE /users/<id> → Delete a user

🧰 Tools Used

Language: Python

Framework: Flask

Testing: Postman / Curl

The app will start at:
http://127.0.0.1:5000

🧪 Example Requests (via Postman)
➕ Create User
POST http://127.0.0.1:5000/users
Body (JSON):

{
  "name": "Alice",
  "email": "alice@example.com"
}

📋 Get All Users

GET http://127.0.0.1:5000/users

✏️ Update User

PUT http://127.0.0.1:5000/users/1
Body (JSON):

{
  "name": "Alice Johnson",
  "email": "alice.j@example.com"
}

❌ Delete User

DELETE http://127.0.0.1:5000/users/1

✨ Learn API fundamentals with Flask!
