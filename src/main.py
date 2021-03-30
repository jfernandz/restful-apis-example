# coding=utf-8
from flask import request

from entities.database_conn import db, app
from entities.Equipment import EquipmentSchema, Equipment


# init Schema
equipment_schema = EquipmentSchema()
equipments_schema = EquipmentSchema(many=True)
db.create_all()


@app.route('/add_equipment', methods=['POST'])
def add_equipment():
    """Adds a new equipment in the 'equipments' table
    """
    name = request.json['name']
    description = request.json['description']
    status = request.json['status']
    exec_path = request.json['exec_path']
    url = request.json['url']

    new_product = Equipment(name, description, status, exec_path, url)
    db.session.add(new_product)
    db.session.commit()

    return equipment_schema.jsonify(new_product)


@app.route('/equipments', methods=['GET'])
def get_equipments():
    """Get a list of all existent equipments
    """
    equipments = Equipment.query.all()
    results = equipments_schema.dump(equipments)
    print(results)
    return {"Equipments": results}


@app.route('/equipment/<int:pk>', methods=['GET'])
def get_equipment(pk):
    """Gets a particular equipment using for a given
    primary key
    """
    equipment_query = Equipment.query.get(pk)
    equipment_result = equipment_schema.dump(equipment_query)
    return {"equipment": equipment_result}


# Run sever
if __name__ == '__main__':
    app.run(debug=True)
