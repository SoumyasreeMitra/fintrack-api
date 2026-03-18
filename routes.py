from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, create_access_token
from models import db, Transaction

api = Blueprint('api', __name__)

@api.route('/login', methods=['POST'])
def login():
    data = request.json
    token = create_access_token(identity=data['username'])
    return jsonify({"token": token})

@api.route('/transactions', methods=['POST'])
@jwt_required()
def add_transaction():
    data = request.json
    t = Transaction(**data)
    db.session.add(t)
    db.session.commit()
    return jsonify({"message": "Transaction added"}), 201

@api.route('/transactions/<user>', methods=['GET'])
@jwt_required()
def get_transactions(user):
    transactions = Transaction.query.filter_by(user=user).all()
    return jsonify([t.to_dict() for t in transactions])

@api.route('/summary/<user>', methods=['GET'])
@jwt_required()
def get_summary(user):
    transactions = Transaction.query.filter_by(user=user).all()
    income = sum(t.amount for t in transactions if t.type == 'income')
    expense = sum(t.amount for t in transactions if t.type == 'expense')
    return jsonify({
        "income": income,
        "expense": expense,
        "balance": income - expense
    })

@api.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@api.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500