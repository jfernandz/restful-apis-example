# coding=utf-8
from flask import request, jsonify
from entities.database_conn import db, app
from entities.Equipment import EquipmentSchema, Equipment

# init Schema
product_schema = EquipmentSchema()
# product_schema = ProductSchema(strict=True)
# products_schema = ProductSchema(strict=True, many=True)
db.create_all()


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
