from flask import Flask, request, json, jsonify
from main import db
from models import *


def add_new_book_note(bookid, userid):
    note = json.loads(request.data)
    n = Notes(bookid, userid, note["text"])
    db.session.add(n)
    db.session.commit()
    return "Note added"


def return_book_notes(bookID):
    notes = Notes.query.filter_by(bookid=bookID)
    if notes:
        return jsonify([n.to_dict() for n in notes])
    else:
        return 'Book ID does not exist'


def update_book_note(bookID, noteid):
    note = Notes.query.filter_by(noteid=noteid).first()
    if note:
        data = json.loads(request.data)
        note.text = data["note"]
        db.session.commit()
        return 'Note Updated'
    else:
        return 'Note does not exist'

def delete_book_note(bookID, noteid):
    note = Notes.query.filter_by(noteid=noteid).first()
    if note:
        db.session.delete(note)
        db.session.commit()
        return 'Note Deleted'
    else:
        return 'Note does not exist'