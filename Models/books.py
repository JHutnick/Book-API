from flask import Flask, request, json, jsonify
from main import db
from models import *
from datetime import date

def add_book(book):

    b = Book(book["author"], book["genre"], book["bookname"], book["publishedDate"], book["loanstatus"])
    db.session.add(b)
    db.session.commit()

    return "Book added"


def get_books():
    return jsonify([b.to_dict() for b in Book.query.all()])



def delete_book(deleteid):
    b = Book.query.filter_by(bookid=deleteid).first()
    print("You are about to delete book " + b.bookname)
    db.session.delete(b)
    db.session.commit()
    return "Book deleted"


def get_book(bookID):
    b = Book.query.filter_by(bookid=bookID).first()
    return jsonify(b.to_dict())
    # fix to_dict function


def books_by_author(author):
    book_list = Book.query.filter_by(author=author).all()
    return jsonify([b.to_dict() for b in book_list])

def books_by_genre(genre):
    book_list = Book.query.filter_by(genre=genre).all()
    return jsonify([b.to_dict() for b in book_list])


def get_by_date(dates):
    params = dates.parse_args()
    book_list = Book.query
    if params['startdate']:
        book_list = book_list.filter(Book.publishedDate >= params['startdate'])
    if params['enddate']:
        book_list = book_list.filter(Book.publishedDate <= params['enddate'])

    return jsonify([b.to_dict() for b in book_list])


def new_loan_status(bookID, userID):
    # if book ID is loaned then give error
    loaned = UserBookAssociation.query.filter_by(bookid=bookID).first()
    if not loaned:
        check_out = UserBookAssociation(bookID, userID)
        db.session.add(check_out)
        db.session.commit()
        return jsonify(check_out.to_dict())
    else:
        return 'Book is already loaned'


def return_book(bookID):
    # if book ID is not loaned then give error
    # change book ID as returned
    book = UserBookAssociation.query.filter_by(bookid=bookID).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return 'Book returned'
    else:
        return 'Book is not loaned'


def get_all_loaned_books():
    return jsonify([u.to_dict() for u in UserBookAssociation.query.all()])


def get_user_loaned(userID):
    # if book ID is loaned then give error
    books = UserBookAssociation.query.filter_by(userid=userID)
    if books:
        return jsonify([b.to_dict() for b in books])
    else:
        return 'No Books loaned for user'


def general_search(parser):
    params = parser.parse_args()
    book_list = Book.query
    if params['author']:
        book_list = book_list.filter_by(author=params['author'])
    if params['genre']:
        book_list = book_list.filter_by(genre=params['genre'])
    if params['startdate']:
        book_list = book_list.filter(Book.publishedDate >= params['startdate'])
    if params['enddate']:
        book_list = book_list.filter(Book.publishedDate <= params['enddate'])

    return jsonify([b.to_dict() for b in book_list])
