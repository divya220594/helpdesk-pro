from datetime import datetime
from app import db

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(30), default="Open")
    priority = db.Column(db.String(30), default="Medium")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
