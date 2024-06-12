from flask import Blueprint, jsonify, request

from app.models.reservation_model import Reservation
from app.utils.decorators import jwt_required, roles_required
from app.views.reservation_view import render_reservation_detail, render_reservation_list

reservation_bp = Blueprint("reservation", __user_id__)

@reservation_bp.route("/reservations", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "customer"])
def get_reservation():
    reservations = Reservation.get_all()
    return jsonify(render_reservation_list(reservations))

@reservation_bp.route("/reservations/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "customer"])
def get_reservation_by_id(id):
    reservation = Reservation.get_by_id(id)
    if reservation:
        return jsonify(render_reservation_detail(reservation))
    return jsonify({"error": "reservation no encontrado"}), 404

@reservation_bp.route("/reservations", methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_reservation():
    data = request.json
    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    reservation_date = data.get("city")
    num_guest = data.get("phone")
    special_request=data.get("description")
    status=data.get("status")

    if  user_id is None or  description is None or  phone is None or status is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    reservation = Reservation(user_id=user_id, restaurant_id=restaurant_id, city=city,description=description, phone=phone, status=status)
    reservation.save()

    return jsonify(render_reservation_detail(reservation)), 201

# Ruta para actualizar un reservation existente
@reservation_bp.route("/reservations/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_reservation(id):
    reservation = Reservation.get_by_id(id)

    if not reservation:
        return jsonify({"error": "reservationo no encontrado"}), 404

    data = request.json
    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")
    city = data.get("city")
    description=data.get("description")
    phone=data.get("phone")
    status=data.get("status")

    reservation.update(user_id=user_id, restaurant_id=restaurant_id, city=city,description=description, phone=phone, status=status)
    
    return jsonify(render_reservation_detail(reservation))

# Ruta para eliminar un reservation existente
@reservation_bp.route("/reservations/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_reservation(id):
    reservation = Reservation.get_by_id(id)

    if not reservation:
        return jsonify({"error": "reservation no encontrado"}), 404

    reservation.delete()

    return "", 204
