from sqlalchemy import ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship, backref

from main import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):
    __tablename__ = 'users'

    userid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String())
    isadmin = db.Column(db.Boolean())
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    phone = db.Column(db.Integer)

    def __init__(self, firstname, lastname, email, phone, isadmin):
        self.email = email
        self.isadmin = isadmin
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone

    def to_dict(self):
        return {
            "userid": self.userid,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "isadmin": self.isadmin,
            "phone": self.phone,
        }



class Book(db.Model):
    __tablename__ = 'books'

    bookid = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    genre = db.Column(db.String)
    bookname = db.Column(db.String)
    publishedDate = db.Column(db.DateTime)
    loanstatus = db.Column(db.Boolean)
    userid = db.Column(db.Integer)

    def __init__(self, author, genre, bookname, publishedDate, loanstatus):
        self.author = author
        self.genre = genre
        self.bookname = bookname
        self.publishedDate = publishedDate
        self.loanstatus = loanstatus
        self.userid = 0

    def to_dict(self):
        return {
            "bookid": self.bookid,
            "author": self.author,
            "genre": self.genre,
            "bookname": self.bookname,
            "publishedDate": self.publishedDate,
            "loanstatus": self.loanstatus,
            "userid": self.userid
        }


class Notes(db.Model):
    __tablename__ = 'notes'
    noteid = db.Column(db.Integer, primary_key=True)
    bookid = db.Column(db.Integer)
    userid = db.Column(db.Integer)
    text = db.Column(db.String)

    def __init__(self, bookid, userid, text):
        self.bookid = bookid
        self.userid = userid
        self.text = text

    def to_dict(self):
        return {
            "noteid": self.noteid,
            "bookid": self.bookid,
            "userid": self.userid,
            "text": self.text
        }


class UserBookAssociation(db.Model):
    __tablename__ = 'associations'

    checkoutid = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer)
    bookid = db.Column(db.Integer)

    def __init__(self, bookid, userid):
        self.userid = userid
        self.bookid = bookid

    def to_dict(self):
        return {
            "checkoutid": self.checkoutid,
            "bookid": self.bookid,
            "userid": self.userid
        }
