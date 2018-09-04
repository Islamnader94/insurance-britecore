from app import db
import datetime


class Field(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, name, number, date):
        self.name = name
        self.number = number
        self.date = datetime.datetime.strptime(date, '%Y-%m-%d').date()


class Risk(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)

    def __init__(self, name):
        self.name = name


class FieldType(db.Model):
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    field_id_fk = db.Column(db.Integer, db.ForeignKey('field.id'))


def create_fields(new_name, new_number, new_date):

    field = Field(new_name, new_number, new_date)

    # add this fields to the database
    db.session.add(field)

    # Save all pending changes to the database
    db.session.commit()

    return field


def create_risk(new_name):

    risk = Risk(new_name)

    db.session.add(risk)

    db.session.commit()

    return risk


def delete_fields(old_name, old_number, old_date):

    field = Field(old_name, old_number, old_date)

    db.session.delete(field)

    db.session.commit()

    return "feilds deleted"


if __name__ == "__main__":

    # Run this file directly to create the database tables.
    print ("Creating database tables...")
    db.create_all()
    print ("Done!")
