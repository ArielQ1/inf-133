from flask import Blueprint, request, jsonify, redirect, url_for, flash
from flask_login import login_required, current_user
from models.dulce_model import Dulce
from views import dulce_view

from utils.decorators import role_required

dulce_bp = Blueprint("dulce", __name__)

@dulce_bp.route("/dulces", methods=["GET", "POST"])
@login_required
def list_dulces():
    dulces = Dulce.get_all()
    return dulce_view.list_dulces(dulces)

@dulce_bp.route("/dulces/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_dulce():
    if request.method == "POST":
        marca = request.form["marca"]
        peso = request.form["peso"]
        sabor = request.form["sabor"]
        origen = request.form["origen"]
        dulce = Dulce(marca, peso, sabor, origen)
        dulce.save()
        flash("Dulce creado exitosamente", "success")
        return redirect(url_for("dulce.list_dulces"))
    else:
        return dulce_view.create_dulce()
    
@dulce_bp.route("/dulces/<int:id>/update", methods=["GET", "POST"])
@login_required
@role_required("admin")
def update_dulce(id):
    dulce = Dulce.get_by_id(id)
    if not dulce:
        return "Dulce no encontrado", 404
    if request.method == "POST":
        marca = request.form["marca"]
        peso = request.form["peso"]
        sabor = request.form["sabor"]
        origen = request.form["origen"]
        dulce.update(marca, peso, sabor, origen)
        flash("Dulce actualizado exitosamente", "success")
        return redirect(url_for("dulce.list_dulces"))
    return dulce_view.update_dulce(dulce)

@dulce_bp.route("/dulces/<int:id>/delete")
@login_required
@role_required("admin")
def delete_dulce(id):
    dulce = Dulce.get_by_id(id)
    if not dulce:
        return "Dulce no encontrado", 404
    if current_user.has_role("admin"):
        dulce.delete()
        flash("Dulce eliminado exitosamente", "success")
        return redirect(url_for("dulce.list_dulces"))
    else:
        return jsonify({"message":"Unautorized"}), 403