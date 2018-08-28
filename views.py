from flask import render_template, request, jsonify

from models import Field, Risk, create_fields, create_risk
from app import app, db


@app.route('/')
def index():

    return render_template('index.html')


# retrive all fields and risks into template review.html
@app.route('/review')
def review():

    field = Field.query.all()
    risk = Risk.query.all()

    return render_template('review.html', field=field, risk=risk)

# retriving single risk by id
@app.route('/risk/<id>', methods=['GET'])
def getby_id():
    risk = Risk.query.filter_by(id=id).first()
    return user_schema.jsonify(risk)

# adding fields
@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'GET':
        return render_template('add.html')


    field_name = request.form.get('name_field')
    field_number = request.form.get('number_field')
    field_date = request.form.get('date_field')

    field = create_fields(field_name, field_number, field_date)
    return render_template('add.html', field=field)

# adding risk type

@app.route('/addrisk', methods=['GET', 'POST'])
def addrisk():

    if request.method == 'GET':
        return render_template('addrisk.html')


    risk_name = request.form.get('name_risk')

    risk = create_risk(risk_name)
    return render_template('addrisk.html', risk=risk)


@app.route('/delete', methods=['DELETE'])
def delete():

    if request.method == 'DELETE':
       field = delete_fields(old_name, oldnumber, old_date)

#error handling routes
#@app.errorhandler(404)
#def not_found_error(error):
    #return render_template('404.html'), 404

#@app.errorhandler(500)
#def internal_error(error):
    #db.session.rollback()
    #return render_template('500.html'), 500
