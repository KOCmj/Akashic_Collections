from flask import Blueprint, request, jsonify, render_template, flash
from helpers import token_required
from models import db, User, Book, books_schema, book_schema


api = Blueprint('api', __name__, url_prefix = '/api')


@api.route('/books', methods = ['POST'])
@token_required
def create_user(current_user_token):
    IBSN = request.json['IBSN']
    title = request.json['title']
    author = request.json['author']
    published_date = request.json['published_date']
    category = request.json['category']
    image = request.json['image']
    user_token = current_user_token.token

    print(f'TEST: {current_user_token.token}')

    book = Book(IBSN, title, author, published_date, category, image, user_token=user_token)

    db.session.add(book)
    db.session.commit()

    response = book_schema.dump(book)
    return jsonify(response)

@api.route('/books', methods = ['GET'])
@token_required
def get_user(current_user_token):
    a_user = current_user_token.token
    books = Book.query.filter_by(user_token = a_user).all()
    response = books_schema.dump(books)
    return jsonify(response)

@api.route('/books/<id>', methods = ['GET'])
@token_required
def get_single_user(current_user_token, id):
    book = Book.query.get(id)
    response = book_schema.dump(book)
    return jsonify(response)


@api.route('/books/<id>', methods = ['POST', 'PUT'])
@token_required
def update_user(current_user_token, id):
    book = Book.query.get(id)
    book.IBSN = request.json['IBSN']
    book.title = request.json['title']
    book.author = request.json['author']
    book.published_date = request.json['published_date']
    book.category = request.json['category']
    book.image = request.json['image']
    book.user_token = current_user_token.token

    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)


@api.route('/books/<id>', methods = ['DELETE'])
@token_required
def delete_user(current_user_token, id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    response = book_schema.dump(book)
    return jsonify(response)

