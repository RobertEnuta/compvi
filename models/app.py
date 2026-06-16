from flask import Flask, request,jsonify
import os
from fileinput import filename
from dotenv import load_dotenv
import apiGateway as model
# import bcrypt
# import jwt
# import datetime

load_dotenv() 
app = Flask(__name__)
# app.config["SECRET_KEY"] = os.getenv("APP_KEY")

@app.route("/transcript", methods=["POST"])
def transcript():
    file = request.files['file']
    content_type = request.content_type 
    if file:
        filename = file.filename
        file.save(f"./{filename}")
        print (model.transcription("./output.wav"))


    return filename #model.transcription(t)


@app.route("/",methods=["GET"])
def home():
    return "home"





if __name__ == '__main__':
    app.run(debug=True)