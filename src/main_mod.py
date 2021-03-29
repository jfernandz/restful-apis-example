import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# INIT DB
db = SQLAlchemy(app)

# init Marshmallow
ma = Marshmallow(app)

# product class/model


class Equipment(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    status = db.Column(db.Integer)
    exec_path = db.Column(db.String(200))

    def __init__(self, name, description, status, exec_path):
        self.name = name
        self.description = description
        self.status = status
        self.exec_path = exec_path


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'name', 'description', 'status', 'exec_path')


# init Schema
product_schema = ProductSchema()
# product_schema = ProductSchema(strict=True)
# products_schema = ProductSchema(strict=True, many=True)


# create_product:
@app.route('/add_equipment', methods=['POST'])
def add_equipment():
    name = request.json['name']
    description = request.json['description']
    status = request.json['status']
    exec_path = request.json['exec_path']

    new_product = Equipment(name, description, status, exec_path)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


@app.route('/', methods=['GET'])
def get_equipments():
    results = db.session.query(Equipment).all()
    return jsonify(results)


# Run sever
if __name__ == '__main__':
    app.run(debug=True)
