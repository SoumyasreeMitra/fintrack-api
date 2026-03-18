from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50))
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(10))  # income or expense
    date = db.Column(db.String(20))

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user,
            "category": self.category,
            "amount": self.amount,
            "type": self.type,
            "date": self.date
        }