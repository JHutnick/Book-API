from flask import Flask, request, json, jsonify
from main import db
from models import *


def print_users():
    return jsonify([u.to_dict() for u in User.query.all()])

def print_user(searchID):
    return jsonify(User.query.filter_by(userid=searchID).first().to_dict())

def delete_user(deleteID):
    u = User.query.filter_by(userid=deleteID).first()
    print("You are about to delete user " + u.firstname)
    db.session.delete(u)
    db.session.commit()
    return "User deleted"

def get_user_books(userID):
    return jsonify(User.query.filter_by(userid=userID).first().booksCheckedOut)

def add_user(user):
    u = User(user["email"], user["firstname"], user["lastname"], user["phone"], False)
    db.session.add(u)
    db.session.commit()
    # print (request.data)
    # print (user)
    return "Created"



