from flask import Flask, request, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from email_maker import *
from flask_cors import CORS
from flask_restplus import reqparse


app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://ctsedpyblanarh:ca4fc9c00c0a608a7ba77d815a013df113f22281e380fefcf2ae55e1d2934861@ec2-54-235-252-23.compute-1.amazonaws.com:5432/d674vb7knohkqm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import *
from Models.users import *
from Models.books import *
from Models.notes import *
# Default route for app
@app.route('/')
def home():
    # str([u.firstname for u in User.query.all()])
    return "Welcome to MSD Library Project"


# GETS and returns all users in JSON
@app.route('/users/', methods=['GET'])
def get_users():
    return print_users()


# GETS and returns user by specific userId
@app.route('/users/<searchid>', methods=['GET'])
def print_user(searchid):
    return jsonify(User.query.filter_by(userid=searchid).first().to_dict())


# DELETES user by specific userId
@app.route('/users/<deleteID>', methods=['DELETE'])
def delete_user_by_id(deleteID):
    return delete_user(deleteID)


# Prints a list of all the books a User has checked out
@app.route('/users/<userID>/books/', methods=['GET'])
def get_books_by_user_id(userID):
    return get_user_books(userID)


# POSTS a new user to the system
@app.route('/users/', methods=['POST'])
def add_new_user():
    user = json.loads(request.data)
    return add_user(user)


# POSTS a new book to the system
@app.route('/books/', methods=['POST'])
def add_new_book():
    book = json.loads(request.data)
    return add_book(book)

# GETS and returns all the books in JSON
@app.route('/books/', methods=['GET'])
def get_all_books():
    return get_books()


# DELETES a specific book in the system
@app.route('/books/<deleteid>', methods=['DELETE'])
def delete_book_by_id(deleteid):
    return delete_book(deleteid)


# GET book by bookID
@app.route('/books/bookid/<bookID>', methods=['GET'])
def get_book_by_ID(bookID):
    return get_book(bookID)


# GETS and returns all the books with the matching author
@app.route('/books/author/<author>', methods=['GET'])
def get_books_by_author(author):
    return books_by_author(author)


# GET books by genre
@app.route('/books/genre/<genre>', methods=['GET'])
def get_book_by_genre(genre):
    return books_by_genre(genre)


# GETS and returns all the books with the publishedDate
@app.route('/books/published_date', methods=['GET'])
def get_books_by_date():
    parser = reqparse.RequestParser()
    parser.add_argument('startdate', type=str, help='Start date to search in yyyy-mm-dd format')
    parser.add_argument('enddate', type=str, help='End date to search in yyyy-mm-dd format')
    return get_by_date(parser)


# PUT new loan status
@app.route('/books/<bookID>/loaned/<userID>', methods=['PUT'])
def update_loan_status(bookID, userID):
    return new_loan_status(bookID, userID)


# DELETE
@app.route('/books/<bookID>/returned/', methods=['DELETE'])
def update_returned(bookID):
    return return_book(bookID)


# POST new book note
@app.route('/books/<bookid>/note/<userid>', methods=['POST'])
def add_book_note(bookid, userid):
    return add_new_book_note(bookid, userid)


# GET Book notes
@app.route('/books/<bookID>/note', methods=['GET'])
def get_book_note(bookID):
    return return_book_notes(bookID)


# PUT and update the books note
@app.route('/books/<bookid>/note/<noteid>', methods=['PUT'])
def update_note(bookid, noteid):
    return update_book_note(bookid, noteid)


# PUT and update the books note
@app.route('/books/<bookid>/note/<noteid>', methods=['DELETE'])
def delete_note(bookid, noteid):
    return delete_book_note(bookid, noteid)


# GET list of loaned books
@app.route('/books/loaned/', methods=['GET'])
def get_loaned_books():
    return get_all_loaned_books()


# Get all loaned books by user
@app.route('/books/loaned/<userID>', methods=['GET'])
def get_user_loaned_books(userID):
    return get_user_loaned(userID)


#GET list of books matching parameters
@app.route('/books/search/', methods=['GET'])
def search_by_params():
    parser = reqparse.RequestParser()
    parser.add_argument('author', type=str)
    parser.add_argument('genre', type=str)
    parser.add_argument('startdate', type=str, help='Start date to search in yyyy-mm-dd format')
    parser.add_argument('enddate', type=str, help='End date to search in yyyy-mm-dd format')
    return general_search(parser)


# Main method to run
if __name__ == '__main__':
    app.run()
