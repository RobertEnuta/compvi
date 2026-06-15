from flask import Flask, request,jsonify
import Connector as conn
import os
from dotenv import load_dotenv
import bcrypt
import jwt
import datetime

load_dotenv() 
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("APP_KEY")



@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username") 
    UUID = data.get("UUID") 
    password = data.get("password")
    password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return conn.create_user(UUID,password,username)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    UUID = data.get("UUID") 
    password = data.get("password")
    u = conn.read_users({"name":username})[0]
    print(u)
    if not bcrypt.checkpw(password.encode("utf-8"), u["password"]):
        return jsonify({"error": "Invalid credentials"}), 401
    # create JWT token with expiry
    token = jwt.encode({
        "username": username,
        "exp": datetime.datetime.now() + datetime.timedelta(hours=4)
    }, app.config["SECRET_KEY"], algorithm="HS256")

    return (conn.update_user({"_id":UUID},token) + "  " + token )

@app.route("/logout", methods=["POST"])
def logout():
    """Invalidate Token"""
    token = request.headers.get("Authorization").replace("Bearer ", "")
    # query for the user with this token and remove it
    conn.update_user({"token":token},None)

    return jsonify({"message": "Logged out"})

@app.route("/luser", methods=["GET"])
def users():
    """List all users"""
    users = []
    admin = request.headers.get("admin")
    if not admin: 
        return jsonify({"error": "Not an admin"}), 401
    username = request.args.get("username") 
    password = request.args.get("password")
    password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    UUID = request.args.get("UUID")
    query = request.args.get("query",default="") 
    if not conn.login_user(UUID,password,username):
        return jsonify({"error": "User doesnt exist"}), 401
    if query != "":
        for u in conn.read_users({"name":query}):
            u.pop("_id")
            users.append(u)
        else :
            for u in conn.read_users():
                u.pop("_id")
                users.append(u)
    return users

# TOKEN REQUIRED DECORATOR
def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token missing"}), 401

        try:
            token = token.replace("Bearer ", "")
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = conn.read_users({"token":token})[0]

            # optional DB validation (token stored per user)
            if not current_user or current_user.get("token") != token:
                return jsonify({"error": "Invalid token"}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401

        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

        return func(current_user, *args, **kwargs)

    wrapper.__name__ = func.__name__
    return wrapper


@app.route("/training", methods=["POST"])
@token_required
def post_training(current_user):
    UUID = current_user["_id"] 
    eye = request.get_json(silent=True) or {} 
    feedback = request.args.get("fb") 
    return conn.create_training(UUID,eye,feedback)


@app.route("/prog", methods=["GET"])
@token_required
def get_prog(current_user):
    list = []
    for item in conn.read_prog(current_user["_id"]):
        item.pop("_id",None) 
        list.append(item)
    print (list)
    return list


@app.route("/del-user", methods=["POST"])
@token_required
def del_acc(current_user):
    conn.del_prog(current_user["_id"])
    conn.del_user({"UUID":current_user["_id"]})
    return "Your account has been deleted"


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()