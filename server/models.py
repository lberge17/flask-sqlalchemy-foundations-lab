from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model):
    __tablename__ = 'earthquakes'

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float)
    location = db.Column(db.String)
    year = db.Column(db.Integer)

    def __repr__(self):
        return f'<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>'

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'location': self.location,
    #         'magnitude': self.magnitude,
    #         'year': self.year
    #     }
