from . import db
from datetime import datetime

class Client(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    display_id = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    source = db.Column(db.String(255))
    status = db.Column(db.String(255), nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    sessions = db.relationship('Session', backref='client', lazy=True, cascade='all, delete-orphan')
    documents = db.relationship('Document', backref='client', lazy=True, cascade='all, delete-orphan')

    def __init__(self, name, email, phone=None, source=None, status="Initial Contact", notes=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.source = source
        self.status = status
        self.notes = notes

    def to_dict(self):
        return {
            "id": self.display_id,  # Return display_id as the public ID
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "source": self.source,
            "status": self.status,
            "notes": self.notes,
            "createdAt": self.created_at.isoformat() if self.created_at else None,
            "updatedAt": self.updated_at.isoformat() if self.updated_at else None,
        }
