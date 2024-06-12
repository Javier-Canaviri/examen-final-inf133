from flask import Blueprint, jsonify, request

from app.models.restaurant_model import Restaurant
from app.utils.decorators import jwt_required, roles_required
from app.views.restaurant_view import render_restaurant_detail, render_restaurant_list

restaurant_bp = Blueprint("restaurant", __name__)

@restaurant_bp.route("/restaurants", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "customer"])
def get_restaurant():
    restaurants = Restaurant.get_all()
    return jsonify(render_restaurant_list(restaurants))

@restaurant_bp.route("/restaurants/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "customer"])
def get_restaurant_by_id(id):
    restaurant = Restaurant.get_by_id(id)
    if restaurant:
        return jsonify(render_restaurant_detail(restaurant))
    return jsonify({"error": "restaurant no encontrado"}), 404

@restaurant_bp.route("/restaurants", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_restaurant():
    data = request.json
    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    phone = data.get("phone")
    description=data.get("description")
    rating=data.get("rating")

    if  name is None or  description is None or  phone is None or rating is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    restaurant = Restaurant(name=name, address=address, city=city,description=description, phone=phone, rating=rating)
    restaurant.save()

    return jsonify(render_restaurant_detail(restaurant)), 201

# Ruta para actualizar un restaurant existente
@restaurant_bp.route("/restaurants/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_restaurant(id):
    restaurant = Restaurant.get_by_id(id)

    if not restaurant:
        return jsonify({"error": "restauranto no encontrado"}), 404

    data = request.json
    name = data.get("name")
    address = data.get("address")
    city = data.get("city")
    description=data.get("description")
    phone=data.get("phone")
    rating=data.get("rating")

    restaurant.update(name=name, address=address, city=city,description=description, phone=phone, rating=rating)
    
    return jsonify(render_restaurant_detail(restaurant))

# Ruta para eliminar un restaurant existente
@restaurant_bp.route("/restaurants/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_restaurant(id):
    restaurant = Restaurant.get_by_id(id)

    if not restaurant:
        return jsonify({"error": "restaurant no encontrado"}), 404

    restaurant.delete()

    return "", 204






