from flask import Blueprint, request, jsonify
from models.dulce_model import Dulce
from views.dulce_view import render_dulce_detail, render_dulce_list
from utils.decorators import jwt_required, roles_required

#Crear un blueprint para el controlador
dulce_bp = Blueprint("dulce", __name__)



@dulce_bp.route("/dulces", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_dulces():
    dulces = Dulce.get_all()
    return jsonify(render_dulce_list(dulces))


@dulce_bp.route("/dulces/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_dulce(id):
    dulce = Dulce.get_by_id(id)
    if dulce:
        return jsonify(render_dulce_detail(dulce))
    return jsonify({"error":"dulce no encontrado"}), 404

@dulce_bp.route("/dulces", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_dulce():
    data = request.json
    marca = data.get("marca")
    peso = data.get("peso")
    sabor = data.get("sabor")
    origen = data.get("origen")

    #Validadcion simple de datos de entrada
    if not marca or not peso or not sabor or not origen:
        return jsonify({"error":"Faltan datos"}), 400

    dulce = Dulce(marca=marca, peso=peso, sabor=sabor, origen=origen)
    dulce.save()
    return jsonify(render_dulce_detail(dulce)), 201

@dulce_bp.route("/dulces/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_dulce(id):
    dulce = Dulce.get_by_id(id)
    if not dulce:
        return jsonify({"error":"Dulce no encontrado"}), 404
    
    data = request.json
    marca = data.get("marca")
    peso = data.get("peso")
    sabor = data.get("sabor")
    origen = data.get("origen")


    dulce.update(marca=marca, peso=peso, sabor=sabor, origen=origen)
    return jsonify(render_dulce_detail(dulce))


@dulce_bp.route("/dulces/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_animal(id):
    dulce = Dulce.get_by_id(id)
    if not dulce:
        return jsonify({"error":"dulce no encontrado"}),404

    dulce.delete()

    return "", 204

