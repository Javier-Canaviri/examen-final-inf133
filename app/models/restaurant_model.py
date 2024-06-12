from app.database import db

class Restaurant(db.Model):
    __tablename__ = "restaurant"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    

    def __init__(self, name,address, description, phone, rating):
        self.name = name
        self.description = description
        self.address=address
        self.phone=phone
        self.rating=rating
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Restaurant.query.all()

    @staticmethod
    def get_by_id(id):
        return Restaurant.query.get(id)

    def update(self, name=None,address=None, description=None, phone=None, rating=None):
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if description is not None:
            self.description = description
        if phone is not None:
            self.phone=phone
        if rating is not None:
            self.rating=rating
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



