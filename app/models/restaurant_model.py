from app.database import db

class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    adress = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Double, nullable=False)
    
    def __init__(self, name, adress, city, phone, description, rating):
        self.name = name
        self.adress = adress
        self.city = city
        self.description = description
        self.rating = rating

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Restaurant.query.all()

    @staticmethod
    def get_by_id(id):
        return Restaurant.query.get(id)

    def update(self, name=None, adress=None, city=None, phone=None, description=None, rating=None):
        if name is not None:
            self.name = name
        if adress is not None:
            self.addres = adress
        if city is not None:
            self.city = city
        if phone is not None:
            self.phone = phone
        if description is not None:
            self.description = description
        if rating is not None:
            self.rating = rating
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()